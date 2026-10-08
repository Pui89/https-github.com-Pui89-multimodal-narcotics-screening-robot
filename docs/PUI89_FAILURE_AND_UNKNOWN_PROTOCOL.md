# PUI89 Failure, OOD and UNKNOWN Protocol

## Decision states
EXECUTE / SLOW_DOWN / COLLECT_MORE_DATA / HUMAN_REVIEW / ABORT / UNKNOWN.

## Decision inputs
Confidence, calibrated uncertainty, OOD score, sensor health, cross-modal agreement, evidence consistency, task risk, robot state and communication state.

## Safe abstention
If evidence is insufficient, modalities disagree, a required sensor fails, or the observation is outside the validated envelope, preserve UNKNOWN and route the case to authorized human review.

## Evidence rule
Visual or multimodal screening hypotheses must not be represented as chemical proof. Any validated chemical screening capability must come from an appropriate physical sensing method and its own validation process.

## Robotics rule
Foundation models remain advisory. They cannot bypass deterministic safety validation or directly command motors.
