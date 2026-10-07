from dataclasses import dataclass

@dataclass(frozen=True)
class FlowEstimate:
    mean_speed_px_per_frame: float
    rising_level_px: float

class EnvironmentalFlowEstimator:
    def estimate(self, mean_flow: float, water_level_delta: float) -> FlowEstimate:
        return FlowEstimate(float(mean_flow), float(water_level_delta))
