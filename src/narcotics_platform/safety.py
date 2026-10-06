from dataclasses import dataclass

@dataclass(frozen=True)
class NavigationState:
    localization_confidence: float
    obstacle_distance_m: float
    human_in_exclusion_zone: bool = False
    emergency_stop: bool = False

class SafetyGate:
    def __init__(self, min_localization_confidence: float = 0.70, min_obstacle_distance_m: float = 0.50) -> None:
        self.min_localization_confidence = min_localization_confidence
        self.min_obstacle_distance_m = min_obstacle_distance_m

    def allow_motion(self, state: NavigationState) -> bool:
        return (not state.emergency_stop and not state.human_in_exclusion_zone and state.localization_confidence >= self.min_localization_confidence and state.obstacle_distance_m >= self.min_obstacle_distance_m)
