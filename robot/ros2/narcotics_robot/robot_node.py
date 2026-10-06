from dataclasses import dataclass

@dataclass
class RobotObservation:
    state: str = 'SEARCHING'
    confidence: float = 0.0
    target_visible: bool = False

class ScreeningRobotNode:
    """ROS2-adapter-ready mission state machine.

    The reference implementation contains no direct motor commands.
    A production ROS2 node should publish observations and send only
    safety-gated navigation goals to Nav2.
    """
    def __init__(self):
        self.observation = RobotObservation()

    def update_observation(self, state: str, confidence: float, target_visible: bool):
        self.observation = RobotObservation(state, confidence, target_visible)

    def navigation_allowed(self, safety_gate) -> bool:
        return bool(safety_gate)
