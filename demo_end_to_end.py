"""Synthetic software-only end-to-end screening demo; no sensors or actuators are used."""
import json
from pui89_e2e import EndToEndScreeningPipeline, SensorObservation

T0 = "2026-10-10T00:00:00+00:00"
observations = [
    SensorObservation(
        sensor_id="sim-camera-01", modality="rgb", timestamp=T0, quality=0.92,
        candidate_label="unknown_substance", confidence=0.0,
    ),
    SensorObservation(
        sensor_id="sim-depth-01", modality="depth", timestamp=T0, quality=0.95,
        candidate_label="unknown_substance", confidence=0.0,
    ),
]
result = EndToEndScreeningPipeline().run(observations, case_id="synthetic-demo", now=T0)
print(json.dumps(result.to_dict(), indent=2))
print("\nSynthetic observations only. This is not a narcotics detection result or chemical identification.")
