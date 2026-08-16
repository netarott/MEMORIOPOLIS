#!/usr/bin/env python3
"""第八節「時間の厚み」用の最小実験。

時計上は同じ3時間でも、途中で観測された履歴と初回応答時間が異なる2つの
合成シナリオを比較する。人の能力や心理は評価しない。
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

TIME_FORMAT = "%Y-%m-%d %H:%M"


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
    request_at: datetime
    final_at: datetime
    first_response_at: Optional[datetime]
    events: List[Event]

    @property
    def dwell_minutes(self) -> int:
        """tau: 依頼到着から最終回答までの時計上の滞在時間。"""
        return int((self.final_at - self.request_at).total_seconds() // 60)

    @property
    def first_response_minutes(self) -> Optional[int]:
        """rho: 依頼到着から、依頼者に見える最初の応答までの時間。"""
        if self.first_response_at is None:
            return None
        return int((self.first_response_at - self.request_at).total_seconds() // 60)

    @property
    def history_count(self) -> int:
        """H: 最終回答までに保存された観測イベント数。"""
        return len(self.events)

    @property
    def visible_history_count(self) -> int:
        """依頼者から観測可能だった途中イベント数。"""
        return sum(e.visible_to_requester for e in self.events)


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
    for events in grouped.values():
        events.sort(key=lambda e: e.sequence)
    return grouped


def observe(scenario: str, events: List[Event]) -> Observation:
    request = next(e for e in events if e.event_type == "request")
    final = next(e for e in events if e.event_type == "final_response")
    responses = [
        e for e in events
        if e.visible_to_requester and e.event_type != "request"
    ]
    first_response_at = min((e.observed_at for e in responses), default=None)
    history = [e for e in events if e.event_type != "request"]
    return Observation(
        scenario=scenario,
        request_at=request.observed_at,
        final_at=final.observed_at,
        first_response_at=first_response_at,
        events=history,
    )


def write_outputs(observations: List[Observation], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    summary_fields = [
        "scenario",
        "dwell_minutes_tau",
        "first_response_minutes_rho",
        "history_count",
        "visible_history_count",
        "final_state",
    ]
    summary_rows = []
    for o in observations:
        summary_rows.append({
            "scenario": o.scenario,
            "dwell_minutes_tau": o.dwell_minutes,
            "first_response_minutes_rho": o.first_response_minutes,
            "history_count": o.history_count,
            "visible_history_count": o.visible_history_count,
            "final_state": "回答済み",
        })

    with (output_dir / "time_summary.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=summary_fields)
        writer.writeheader()
        writer.writerows(summary_rows)

    history_fields = [
        "scenario", "sequence", "observed_at", "event_type",
        "visible_to_requester", "description",
    ]
    with (output_dir / "time_history.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=history_fields)
        writer.writeheader()
        for o in observations:
            for e in o.events:
                writer.writerow({
                    "scenario": o.scenario,
                    "sequence": e.sequence,
                    "observed_at": e.observed_at.strftime(TIME_FORMAT),
                    "event_type": e.event_type,
                    "visible_to_requester": e.visible_to_requester,
                    "description": e.description,
                })


def main() -> None:
    parser = argparse.ArgumentParser(description="第八節用『同じ三時間』実験")
    parser.add_argument("--input", type=Path, default=Path("time_events.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    args = parser.parse_args()

    grouped = load_events(args.input)
    observations = [observe(name, events) for name, events in sorted(grouped.items())]
    write_outputs(observations, args.output_dir)

    print("=== 第八節 同じ三時間／最小実験 ===")
    for o in observations:
        rho = "応答なし" if o.first_response_minutes is None else f"{o.first_response_minutes}分"
        print(
            f"{o.scenario}: 滞在時間 tau={o.dwell_minutes}分 / "
            f"初回応答 rho={rho} / 履歴={o.history_count}件 / "
            f"依頼者に見える履歴={o.visible_history_count}件"
        )

    if len(observations) == 2:
        a, b = observations
        print("---")
        print(f"時計時間は同じ: {a.dwell_minutes == b.dwell_minutes}")
        print(f"履歴は同じ: {a.history_count == b.history_count}")
        print(
            "初回応答時間は同じ: "
            f"{a.first_response_minutes == b.first_response_minutes}"
        )


if __name__ == "__main__":
    main()
