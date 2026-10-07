from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

@dataclass
class EvidenceRecord:
    event_id: str
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    sensor_sources: list[str] = field(default_factory=list)
    observations: dict[str, Any] = field(default_factory=dict)
    reviewer_required: bool = True

def make_evidence_record(event_id: str, sensor_sources: list[str], observations: dict[str, Any]) -> EvidenceRecord:
    return EvidenceRecord(event_id, sensor_sources=list(sensor_sources), observations=dict(observations))
