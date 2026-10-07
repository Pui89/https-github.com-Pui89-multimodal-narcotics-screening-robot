"""Model lifecycle governance state machine."""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
class ModelStage(str, Enum):
    CANDIDATE="CANDIDATE"; VALIDATION="VALIDATION"; CALIBRATION="CALIBRATION"
    SAFETY_REVIEW="SAFETY_REVIEW"; APPROVED="APPROVED"; DEPLOYED="DEPLOYED"
    MONITORED="MONITORED"; RETIRED="RETIRED"
_ALLOWED={ModelStage.CANDIDATE:{ModelStage.VALIDATION},ModelStage.VALIDATION:{ModelStage.CALIBRATION,ModelStage.RETIRED},
ModelStage.CALIBRATION:{ModelStage.SAFETY_REVIEW,ModelStage.RETIRED},ModelStage.SAFETY_REVIEW:{ModelStage.APPROVED,ModelStage.RETIRED},
ModelStage.APPROVED:{ModelStage.DEPLOYED,ModelStage.RETIRED},ModelStage.DEPLOYED:{ModelStage.MONITORED,ModelStage.RETIRED},
ModelStage.MONITORED:{ModelStage.RETIRED,ModelStage.DEPLOYED},ModelStage.RETIRED:set()}
@dataclass
class ModelLifecycle:
    model_id:str; version:str; stage:ModelStage=ModelStage.CANDIDATE; notes:list[str]|None=None
    def transition(self,target:ModelStage,note:str="")->None:
        if target not in _ALLOWED[self.stage]: raise ValueError(f"invalid model transition: {self.stage} -> {target}")
        self.stage=target
        if note:
            if self.notes is None:self.notes=[]
            self.notes.append(note)
    def deployment_allowed(self)->bool:return self.stage in {ModelStage.APPROVED,ModelStage.DEPLOYED,ModelStage.MONITORED}
