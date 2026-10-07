# Robustness Benchmark

Use authorized recorded or simulated observations to test controlled failure modes.

Scenarios:
- normal observation
- low illumination
- motion blur
- missing RGB
- missing depth
- missing thermal/NIR
- missing LiDAR
- timestamp skew
- sensor disagreement
- unfamiliar/OOD observation

For each scenario record:
- scenario ID
- available modalities
- expected safe behavior
- prediction
- confidence
- uncertainty
- abstention/review decision
- latency
- safety-gate status

The benchmark must never require a system to infer hidden internal-body state. The desired behavior under uncertainty is abstention or human review.
