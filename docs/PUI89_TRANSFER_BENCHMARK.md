# PUI89 Cross-Environment Transfer Benchmark

Test whether the same embodied-AI interfaces transfer between agriculture, disaster response and security/inspection.

## Shared representation
Observation → Evidence → Object → Geometry → State → Uncertainty → Action proposal → Safety decision.

## Experiments
- zero-shot transfer;
- few-shot adaptation;
- fine-tuning efficiency;
- calibration degradation;
- OOD detection;
- safe abstention;
- sensor-failure recovery;
- planning success;
- safety-gate rejection.

## Protocol
Freeze source training, evaluate a held-out target domain, record all hardware/model settings, inject OOD and degraded-sensor scenarios, compare with a target-domain baseline and publish failure cases.

Transfer performance does not transfer safety authorization. Every deployment domain requires independent safety validation.
