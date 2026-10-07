from dataclasses import dataclass, field
from typing import Mapping

@dataclass(frozen=True)
class SensorStatus:
    name: str
    available: bool = True
    quality: float = 1.0
    synchronized: bool = True
    calibration_id: str | None = None
    notes: str = ""

    def __post_init__(self) -> None:
        if not 0.0 <= self.quality <= 1.0:
            raise ValueError("quality must be between 0 and 1")

@dataclass(frozen=True)
class QualityReport:
    usable: bool
    aggregate_quality: float
    degraded_modalities: tuple[str, ...] = field(default_factory=tuple)
    missing_modalities: tuple[str, ...] = field(default_factory=tuple)
    reasons: tuple[str, ...] = field(default_factory=tuple)

def assess_sensor_quality(statuses: Mapping[str, SensorStatus], minimum_quality: float = 0.50) -> QualityReport:
    if not 0.0 <= minimum_quality <= 1.0:
        raise ValueError("minimum_quality must be between 0 and 1")
    if not statuses:
        return QualityReport(False, 0.0, reasons=("no sensor status supplied",))
    missing = tuple(name for name, s in statuses.items() if not s.available)
    degraded = tuple(name for name, s in statuses.items() if s.available and s.quality < minimum_quality)
    usable_scores = [s.quality for s in statuses.values() if s.available]
    aggregate = sum(usable_scores) / len(usable_scores) if usable_scores else 0.0
    reasons: list[str] = []
    if missing: reasons.append("one or more modalities are unavailable")
    if degraded: reasons.append("one or more modalities are degraded")
    if any(not s.synchronized for s in statuses.values() if s.available): reasons.append("timestamp synchronization is incomplete")
    usable = bool(usable_scores) and aggregate >= minimum_quality and not any(not s.synchronized for s in statuses.values() if s.available)
    return QualityReport(usable, aggregate, degraded, missing, tuple(reasons))