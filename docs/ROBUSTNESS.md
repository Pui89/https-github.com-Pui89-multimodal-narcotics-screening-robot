# Robustness Test Plan

Evaluate the complete pipeline under controlled perturbations:
- low light and exposure changes
- blur and motion blur
- glare and reflections
- partial occlusion
- sensor dropout
- timestamp skew
- thermal noise
- depth noise
- LiDAR sparsity
- unfamiliar objects and domain shift
- conflicting modalities

For each scenario record model version, sensor configuration, dataset split, perturbation parameters, confidence, abstention rate, latency and reviewer outcome.

Desired behavior under severe uncertainty is abstention, not forced classification.
