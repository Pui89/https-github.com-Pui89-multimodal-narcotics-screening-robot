"""Uncertainty-aware 3D evidence geometry utilities."""
from __future__ import annotations
from dataclasses import dataclass
import math
@dataclass(frozen=True)
class Point3D: x:float; y:float; z:float
@dataclass(frozen=True)
class SpatialEvidence:
    point:Point3D
    covariance_diag:tuple[float,float,float]
    confidence:float
    frame_id:str
    timestamp:float
    def radial_uncertainty(self)->float:return math.sqrt(sum(max(v,0.0) for v in self.covariance_diag))
    def quality(self)->float:return max(0.0,min(1.0,self.confidence/(1.0+self.radial_uncertainty())))
