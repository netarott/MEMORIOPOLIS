#!/usr/bin/env python3
"""第七節用の決定論的な最小状態機械。

標準ライブラリだけで動作する。入力は合成CSVであり、実在の顧客情報を含まない。
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Set


class State(str, Enum):
    UNOBSERVED = "未観測"
    CANDIDATE = "候補"
    UNRESOLVED = "未確定"
    RECOVERY_CANDIDATE = "回復候補"
    RESOLVED = "確定"
    REVIEW = "再確認"


REQUIRED_FOR_UNRESOLVED = {"work_log", "inquiry", "schedule"}
REQUIRED_FOR_RECOVERY = REQUIRED_FOR_UNRESOLVED | {"review", "confirmation"}


@dataclass
class Event:
    scenario: str
    sequence: int
    observed_at: str
    event_type: str
    work_unit_key: str
    source_id: str


@dataclass
class Machine:
    scenario: str
    target_work_unit: str = "WU-001"
    state: State = State.UNOBSERVED
    evidence: Dict[str, List[Event]] = field(default_factory=dict)
    audit: List[dict] = field(default_factory=list)

    def add_event(self, event: Event) -> None:
        """証拠を保存し、許可された遷移を繰り返し評価する。"""
        self.evidence.setdefault(event.event_type, []).append(event)
        before = self.state
        transitions = self._reconcile(event)

        if not transitions:
            self.audit.append(self._row(
                event=event,
                before=before,
                after=self.state,
                action="保持",
                reason=self._holding_reason(event),
            ))

    def _matching_types(self) -> Set[str]:
        """対象作業と一致する証拠種別だけを返す。"""
        return {
            event_type
            for event_type, events in self.evidence.items()
            if any(e.work_unit_key == self.target_work_unit for e in events)
        }

    def _reconcile(self, event: Event) -> int:
        """一つの入力で複数の条件が同時に整う場合も監査ログへ残す。"""
        count = 0
        while True:
            matching = self._matching_types()
            before = self.state

            if self.state == State.UNOBSERVED and "work_log" in matching:
                self.state = State.CANDIDATE
                reason = "対象作業の日報を発見"

            elif self.state == State.CANDIDATE and REQUIRED_FOR_UNRESOLVED <= matching:
                self.state = State.UNRESOLVED
                reason = "日報・問い合わせ・作業予定が同じ作業単位へ接続"

            elif self.state == State.UNRESOLVED and REQUIRED_FOR_RECOVERY <= matching:
                self.state = State.RECOVERY_CANDIDATE
                reason = "レビューと確認記録を含む必要証拠が対象作業で一致"

            else:
                break

            self.audit.append(self._row(
                event=event,
                before=before,
                after=self.state,
                action="遷移",
                reason=reason,
            ))
            count += 1

        return count

    def _holding_reason(self, event: Event) -> str:
        matching = self._matching_types()
        if event.work_unit_key != self.target_work_unit:
            return "記録は保存したが、対象作業が一致しない"
        if self.state == State.UNOBSERVED:
            return "対象作業の日報が未到着"
        if self.state == State.CANDIDATE:
            missing = sorted(REQUIRED_FOR_UNRESOLVED - matching)
            return "未確定へ進む証拠が不足: " + ", ".join(missing)
        if self.state == State.UNRESOLVED:
            missing = sorted(REQUIRED_FOR_RECOVERY - matching)
            return "回復候補へ進む証拠が不足: " + ", ".join(missing)
        return "新しい遷移条件なし"

    def _row(self, event: Event, before: State, after: State, action: str, reason: str) -> dict:
        return {
            "scenario": self.scenario,
            "sequence": event.sequence,
            "observed_at": event.observed_at,
            "source_id": event.source_id,
            "event_type": event.event_type,
            "event_work_unit": event.work_unit_key,
            "state_before": before.value,
            "action": action,
            "state_after": after.value,
            "reason": reason,
        }


def load_events(path: Path) -> List[Event]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return [
        Event(
            scenario=r["scenario"],
            sequence=int(r["sequence"]),
            observed_at=r["observed_at"],
            event_type=r["event_type"],
            work_unit_key=r["work_unit_key"],
            source_id=r["source_id"],
        )
        for r in rows
    ]


def run(input_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    events = load_events(input_path)
    scenarios = sorted({e.scenario for e in events})
    all_audit: List[dict] = []
    summaries: List[dict] = []

    for scenario in scenarios:
        machine = Machine(scenario=scenario)
        scenario_events = sorted(
            (e for e in events if e.scenario == scenario),
            key=lambda e: e.sequence,
        )
        for event in scenario_events:
            machine.add_event(event)

        all_audit.extend(machine.audit)
        summaries.append({
            "scenario": scenario,
            "final_state": machine.state.value,
            "input_count": len(scenario_events),
            "audit_count": len(machine.audit),
            "transition_count": sum(r["action"] == "遷移" for r in machine.audit),
            "held_count": sum(r["action"] == "保持" for r in machine.audit),
        })

    audit_path = output_dir / "audit_log.csv"
    with audit_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(all_audit[0]))
        writer.writeheader()
        writer.writerows(all_audit)

    summary_path = output_dir / "summary.csv"
    with summary_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(summaries[0]))
        writer.writeheader()
        writer.writerows(summaries)

    print("=== 第七節 最小状態機械 ===")
    for s in summaries:
        print(
            f"{s['scenario']}: 最終状態={s['final_state']} / "
            f"入力={s['input_count']} / 遷移={s['transition_count']} / 保持={s['held_count']}"
        )
    print(f"監査ログ: {audit_path}")
    print(f"サマリー: {summary_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="第七節用の最小状態機械")
    parser.add_argument("--input", default="test_events.csv", type=Path)
    parser.add_argument("--output-dir", default=Path("results"), type=Path)
    args = parser.parse_args()
    run(args.input, args.output_dir)


if __name__ == "__main__":
    main()
