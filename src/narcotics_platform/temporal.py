"""Deterministic temporal evidence accumulation."""
from __future__ import annotations
from dataclasses import dataclass
from collections import deque
@dataclass(frozen=True)
class TemporalObservation:
    timestamp: float
    label: str
    confidence: float
    uncertainty: float
    track_id: str|None=None
class TemporalEvidenceBuffer:
    def __init__(self,maxlen:int=16)->None:
        if maxlen<2: raise ValueError("maxlen must be >= 2")
        self._items:deque[TemporalObservation]=deque(maxlen=maxlen)
    def add(self,observation:TemporalObservation)->None: self._items.append(observation)
    def observations(self)->tuple[TemporalObservation,...]: return tuple(self._items)
    def stable_label(self,min_observations:int=3)->str|None:
        if len(self._items)<min_observations: return None
        labels=[x.label for x in self._items]
        counts={label:labels.count(label) for label in set(labels)}
        label,count=max(counts.items(),key=lambda item:item[1])
        return label if count>=min_observations else None
    def temporal_confidence(self)->float:
        if not self._items:return 0.0
        weights=[1.0/max(x.uncertainty,1e-6) for x in self._items]
        return sum(x.confidence*w for x,w in zip(self._items,weights))/sum(weights)
