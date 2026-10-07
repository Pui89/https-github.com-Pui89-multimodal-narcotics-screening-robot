"""Operational monitoring primitives for safe screening deployments."""
from __future__ import annotations
from dataclasses import dataclass, field
from time import monotonic

@dataclass
class RuntimeMetrics:
    frames_seen: int = 0
    frames_dropped: int = 0
    inference_ms: float = 0.0
    queue_depth: int = 0
    cpu_percent: float | None = None
    gpu_percent: float | None = None
    ram_percent: float | None = None
    sensor_health: dict[str, float] = field(default_factory=dict)
    sync_drift_ms: float = 0.0
    ood_rate: float = 0.0
    abstention_rate: float = 0.0
    safety_gate_events: int = 0
    @property
    def fps_drop_rate(self) -> float:
        total=self.frames_seen+self.frames_dropped
        return self.frames_dropped/total if total else 0.0

class RuntimeMonitor:
    def __init__(self)->None:
        self.metrics=RuntimeMetrics()
        self._last_frame=monotonic()
    def record_frame(self,*,inference_ms:float,dropped:bool=False)->None:
        if dropped: self.metrics.frames_dropped+=1
        else:
            self.metrics.frames_seen+=1
            self.metrics.inference_ms=float(inference_ms)
        self._last_frame=monotonic()
    def record_decision(self,*,ood:bool,abstained:bool)->None:
        total=self.metrics.frames_seen or 1
        self.metrics.ood_rate=((self.metrics.ood_rate*(total-1))+int(ood))/total
        self.metrics.abstention_rate=((self.metrics.abstention_rate*(total-1))+int(abstained))/total
    def record_safety_gate(self)->None:
        self.metrics.safety_gate_events+=1
    def snapshot(self)->dict:
        return {"frames_seen":self.metrics.frames_seen,"frames_dropped":self.metrics.frames_dropped,
        "drop_rate":self.metrics.fps_drop_rate,"inference_ms":self.metrics.inference_ms,
        "queue_depth":self.metrics.queue_depth,"cpu_percent":self.metrics.cpu_percent,
        "gpu_percent":self.metrics.gpu_percent,"ram_percent":self.metrics.ram_percent,
        "sensor_health":dict(self.metrics.sensor_health),"sync_drift_ms":self.metrics.sync_drift_ms,
        "ood_rate":self.metrics.ood_rate,"abstention_rate":self.metrics.abstention_rate,
        "safety_gate_events":self.metrics.safety_gate_events}
