"""Human-review decision primitives."""
from __future__ import annotations
from dataclasses import dataclass
from enum import StrEnum
class ReviewDecision(StrEnum):
    ACCEPT="ACCEPT"; REJECT="REJECT"; UNKNOWN="UNKNOWN"; REQUEST_MORE_DATA="REQUEST_MORE_DATA"
@dataclass(frozen=True)
class ReviewRecord:
    event_id:str; decision:ReviewDecision; reviewer:str; rationale:str; timestamp:str; evidence_digest:str
    def validate(self)->None:
        if not self.event_id or not self.reviewer or not self.rationale: raise ValueError("event_id, reviewer and rationale are required")
        if len(self.evidence_digest)!=64: raise ValueError("evidence_digest must be a SHA-256 hex digest")
