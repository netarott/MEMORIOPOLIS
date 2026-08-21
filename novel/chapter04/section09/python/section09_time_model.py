"""MEMORIOPOLIS Chapter 4, Section 9: descriptive two-clock model.

This model observes states. It does not score, rank, or reduce them to Yes/No.
All times and scenario details are synthetic and illustrative.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Scenario:
    key: str
    label: str
    t_internal: float
    t_prepared: float
    t_candidate: Optional[float]
    t_external: Optional[float]
    t_received: Optional[float]
    observations: tuple[str, ...]
    paths_available: tuple[str, ...]
    search_state: str

    @property
    def delta(self) -> Optional[float]:
        """Difference between the external and internal clock start times."""
        if self.t_external is None:
            return None
        return self.t_external - self.t_internal


SCENARIOS = (
    Scenario(
        key="send_now",
        label="すぐ問い合わせる",
        t_internal=0.0,
        t_prepared=0.25,
        t_candidate=None,
        t_external=0.50,
        t_received=0.75,
        observations=(
            "内部設定の一部を確認",
            "外部への問い合わせを開始",
            "回答により探索方向が内部設定側へ寄った",
        ),
        paths_available=(
            "回答内容に沿って内部設定を調べる",
            "追加ログを収集する",
        ),
        search_state="外部回答が探索方向に影響している",
    ),
    Scenario(
        key="investigate",
        label="内部調査を続けてから問い合わせる",
        t_internal=0.0,
        t_prepared=0.25,
        t_candidate=None,
        t_external=3.00,
        t_received=3.25,
        observations=(
            "内部設定を確認",
            "障害の再現を試行",
            "内部設定変更では再現条件が変わらないことを観測",
            "外部から必要な情報の境界が明確になった",
        ),
        paths_available=(
            "外部回答を待つ",
            "内部ログとの対応関係を追加確認する",
        ),
        search_state="外部へ尋ねる範囲が限定されている",
    ),
    Scenario(
        key="branch_candidate",
        label="分岐候補として保持し、内部調査と並行する",
        t_internal=0.0,
        t_prepared=0.25,
        t_candidate=0.50,
        t_external=1.50,
        t_received=1.75,
        observations=(
            "問い合わせを分岐候補として記録",
            "内部調査を継続",
            "遅延時刻と内部ログの対応を確認",
            "外部からのみ得られる情報の境界を記述",
        ),
        paths_available=(
            "内部設定の調査を続ける",
            "外部回答を待つ",
            "回答内容に応じて部品交換試験へ進む",
        ),
        search_state="内部調査と外部問い合わせが並行している",
    ),
)


def fmt_time(value: Optional[float]) -> str:
    return "--" if value is None else f"{value:.2f}h"


def print_items(title: str, items: tuple[str, ...]) -> None:
    print(f"  {title}:")
    for item in items:
        print(f"    - {item}")


def print_observation(s: Scenario) -> None:
    print(f"\n[{s.key}] {s.label}")
    print(f"  internal clock  : {fmt_time(s.t_internal)}")
    print(f"  draft prepared  : {fmt_time(s.t_prepared)}")
    print(f"  branch candidate: {fmt_time(s.t_candidate)}")
    print(f"  external clock  : {fmt_time(s.t_external)}")
    print(f"  receipt record  : {fmt_time(s.t_received)}")
    print(f"  delta           : {fmt_time(s.delta)}")
    print(f"  search state    : {s.search_state}")
    print_items("observed state", s.observations)
    print_items("paths available", s.paths_available)


def main() -> None:
    print("MEMORIOPOLIS / Section 09 / Descriptive two-clock observation")
    print("Synthetic data only. ranking: not evaluated")
    print("delta = t_external - t_internal")
    print("No maturity score, path count, or binary quality flag is used.")

    for scenario in SCENARIOS:
        print_observation(scenario)

    print("\nObservation notes")
    print("- delta describes a difference between clock starts; it is not a score.")
    print("- States are recorded as observations rather than maturity levels.")
    print("- Available paths are named rather than reduced to a count.")
    print("- Search direction is described rather than judged as fixed/unfixed.")
    print("- The model does not rank strategies or people.")


if __name__ == "__main__":
    main()
