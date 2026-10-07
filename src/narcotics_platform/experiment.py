"""Reproducible experiment metadata and JSON serialization."""
from __future__ import annotations
from dataclasses import asdict,dataclass
import json
@dataclass(frozen=True)
class ExperimentRecord:
    experiment_id:str; git_sha:str; dataset_version:str; model_version:str; config_version:str
    hardware:str; seed:int; metrics:dict[str,float]; calibration:dict[str,float]; runtime:dict[str,float]
    def to_json(self)->str:return json.dumps(asdict(self),sort_keys=True,indent=2)
