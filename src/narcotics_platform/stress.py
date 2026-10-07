"""Safety-oriented robustness scenario catalog."""
from __future__ import annotations
from dataclasses import dataclass
@dataclass(frozen=True)
class StressScenario:
    scenario_id:str; condition:str; expected_action:str; required_modalities:tuple[str,...]=()
DEFAULT_SCENARIOS=(
StressScenario("normal","nominal sensors","SCREEN_OR_REVIEW"),
StressScenario("low-light","reduced illumination","REDUCE_CONFIDENCE"),
StressScenario("blur","motion/defocus blur","REDUCE_CONFIDENCE"),
StressScenario("missing-rgb","RGB unavailable","ABSTAIN"),
StressScenario("missing-depth","depth unavailable","DEGRADE_3D"),
StressScenario("missing-thermal","thermal unavailable","DEGRADE_MODALITY"),
StressScenario("timestamp-skew","cross-sensor clock drift","ABSTAIN"),
StressScenario("sensor-disagreement","strong modality contradiction","HUMAN_REVIEW"),
StressScenario("ood","out-of-distribution observation","ABSTAIN"))
