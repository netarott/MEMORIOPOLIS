#!/usr/bin/env python3
"""第八節「時間の厚み」精緻化実験 v2。

同じ時計時間の内側を、内部履歴、依頼者から見える履歴、最終回答前の
可視中間応答へ分ける。件数を成績にせず、人やチームを順位づけない。
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

TIME_FORMAT = "%Y-%m-%d %H:%M"
REQUEST = "request"
FINAL = "final_response"


@dataclass(frozen=True)
class Event:
    scenario: str
    sequence: int
    observed_at: datetime
    event_type: str
    visible_to_requester: bool
    description: str


@dataclass
class Observation:
    scenario: str
    request: Event
    final: Event
    history: List[Event]

    @property
    def tau_minutes(self) -> int:
        """tau: 依頼到着から最終回答までの時計時間。"""
        return minutes_between(self.request.observed_at, self.final.observed_at)

    @property
    def internal_history(self) -> List[Event]:
        """H_internal: requestを除く全履歴。finalを含む。"""
        return list(self.history)

    @property
    def visible_history(self) -> List[Event]:
        """H_visible: requestを除き、依頼者から見えた全履歴。finalを含む。"""
        return [e for e in self.history if e.visible_to_requester]

    @property
    def prefinal_history(self) -> List[Event]:
        """最終回答より前に保存された全履歴。"""
        return [e for e in self.history if e.observed_at < self.final.observed_at]

    @property
    def visible_prefinal_history(self) -> List[Event]:
        """H_visible_pre: 最終回答より前に依頼者から見えた履歴。"""
        return [
            e for e in self.prefinal_history
            if e.visible_to_requester
        ]

    @property
    def rho_any_minutes(self) -> int:
        """rho_any: 最終回答を含む、最初の可視応答までの時間。"""
        first = min(e.observed_at for e in self.visible_history)
        return minutes_between(self.request.observed_at, first)

    @property
    def rho_progress_minutes(self) -> Optional[int]:
        """rho_progress: 最終回答前の最初の可視中間応答までの時間。"""
        if not self.visible_prefinal_history:
            return None
        first = min(e.observed_at for e in self.visible_prefinal_history)
        return minutes_between(self.request.observed_at, first)

    @property
    def has_visible_prefinal_update(self) -> bool:
        """I_visible: 最終回答前に可視中間応答が一度でもあったか。"""
        return bool(self.visible_prefinal_history)

    @property
    def longest_visible_silence_minutes(self) -> int:
        """依頼者から見て、可視イベント間で最長だった沈黙時間。"""
        visible_times = [self.request.observed_at]
        visible_times.extend(e.observed_at for e in self.visible_history)
        visible_times = sorted(set(visible_times))
        return max(
            minutes_between(start, end)
            for start, end in zip(visible_times, visible_times[1:])
        )


def minutes_between(start: datetime, end: datetime) -> int:
    return int((end - start).total_seconds() // 60)


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}


def load_events(path: Path) -> Dict[str, List[Event]]:
    grouped: Dict[str, List[Event]] = {}
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            event = Event(
                scenario=row["scenario"],
                sequence=int(row["sequence"]),
                observed_at=datetime.strptime(row["observed_at"], TIME_FORMAT),
                event_type=row["event_type"],
                visible_to_requester=parse_bool(row["visible_to_requester"]),
                description=row["description"],
            )
            grouped.setdefault(event.scenario, []).append(event)

    for scenario, events in grouped.items():
        events.sort(key=lambda e: (e.sequence, e.observed_at))
        if sum(e.event_type == REQUEST for e in events) != 1:
            raise ValueError(f"{scenario}: request must appear exactly once")
        if sum(e.event_type == FINAL for e in events) != 1:
            raise ValueError(f"{scenario}: final_response must appear exactly once")
        for previous, current in zip(events, events[1:]):
            if current.observed_at < previous.observed_at:
                raise ValueError(f"{scenario}: timestamps are not monotonic")
    return grouped


def observe(scenario: str, events: List[Event]) -> Observation:
    request = next(e for e in events if e.event_type == REQUEST)
    final = next(e for e in events if e.event_type == FINAL)
    if final.observed_at < request.observed_at:
        raise ValueError(f"{scenario}: final response precedes request")
    history = [e for e in events if e.event_type != REQUEST]
    return Observation(scenario, request, final, history)


def optional_minutes(value: Optional[int]) -> str:
    return "" if value is None else str(value)


def write_outputs(observations: List[Observation], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_fields = [
        "scenario",
        "dwell_minutes_tau",
        "first_visible_response_minutes_rho_any",
        "first_visible_prefinal_minutes_rho_progress",
        "has_visible_prefinal_update_I_visible",
        "internal_history_count",
        "visible_history_count_including_final",
        "visible_prefinal_count",
        "longest_visible_silence_minutes",
        "final_state",
        "ranking",
    ]

    with (output_dir / "time_summary_v2.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=summary_fields)
        writer.writeheader()
        for o in observations:
            writer.writerow({
                "scenario": o.scenario,
                "dwell_minutes_tau": o.tau_minutes,
                "first_visible_response_minutes_rho_any": o.rho_any_minutes,
                "first_visible_prefinal_minutes_rho_progress": optional_minutes(
                    o.rho_progress_minutes
                ),
                "has_visible_prefinal_update_I_visible": (
                    1 if o.has_visible_prefinal_update else 0
                ),
                "internal_history_count": len(o.internal_history),
                "visible_history_count_including_final": len(o.visible_history),
                "visible_prefinal_count": len(o.visible_prefinal_history),
                "longest_visible_silence_minutes": o.longest_visible_silence_minutes,
                "final_state": "回答済み",
                "ranking": "評価しない",
            })

    history_fields = [
        "scenario", "sequence", "observed_at", "event_type",
        "visible_to_requester", "is_before_final", "history_layer",
        "description",
    ]
    with (output_dir / "time_history_v2.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=history_fields)
        writer.writeheader()
        for o in observations:
            for e in o.history:
                if e.visible_to_requester:
                    layer = "visible"
                else:
                    layer = "internal_only"
                writer.writerow({
                    "scenario": o.scenario,
                    "sequence": e.sequence,
                    "observed_at": e.observed_at.strftime(TIME_FORMAT),
                    "event_type": e.event_type,
                    "visible_to_requester": e.visible_to_requester,
                    "is_before_final": e.observed_at < o.final.observed_at,
                    "history_layer": layer,
                    "description": e.description,
                })


def display(observations: List[Observation]) -> None:
    print("=== 第八節 時間の厚み／精緻化実験 v2 ===")
    for o in observations:
        rho_progress = (
            "なし" if o.rho_progress_minutes is None
            else f"{o.rho_progress_minutes}分"
        )
        print(
            f"{o.scenario}: tau={o.tau_minutes}分 / "
            f"rho_any={o.rho_any_minutes}分 / "
            f"rho_progress={rho_progress} / "
            f"I_visible={int(o.has_visible_prefinal_update)} / "
            f"H_internal={len(o.internal_history)}件 / "
            f"H_visible_pre={len(o.visible_prefinal_history)}件 / "
            f"最長可視沈黙={o.longest_visible_silence_minutes}分"
        )
    print("---")
    print("時計時間の比較だけでは、時間の内側は記述できない。")
    print("可視イベント数は順位や成績に使用しない。")


def main() -> None:
    parser = argparse.ArgumentParser(description="第八節『時間の厚み』精緻化実験")
    parser.add_argument("--input", type=Path, default=Path("time_events_v2.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    args = parser.parse_args()

    grouped = load_events(args.input)
    observations = [observe(name, events) for name, events in sorted(grouped.items())]
    write_outputs(observations, args.output_dir)
    display(observations)


if __name__ == "__main__":
    main()
