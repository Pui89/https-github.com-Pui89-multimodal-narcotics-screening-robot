"""Framework-neutral service contract for the planned online API."""
from __future__ import annotations
from dataclasses import dataclass
from .monitoring import RuntimeMonitor
from .screening import ScreeningPipeline
@dataclass
class ScreeningService:
    pipeline:ScreeningPipeline; monitor:RuntimeMonitor
    def health(self)->dict:return {"status":"ok","actuator_control":False}
    def metrics(self)->dict:return self.monitor.snapshot()
    def screen(self,observations):
        result=self.pipeline.screen(observations)
        decision=str(getattr(result,"decision",""))
        open_set=str(getattr(result,"open_set",""))
        self.monitor.record_decision(ood="unknown" in open_set.lower(),abstained=decision=="ABSTAIN")
        return result
    def models(self)->dict:return {"screening_models":"registry-managed","actuator_models":"not exposed"}
