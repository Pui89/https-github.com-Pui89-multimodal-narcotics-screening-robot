# Operator interface contract

The operator application should expose live sensor health, synchronized evidence, uncertainty/OOD indicators, screening history, a human-review queue, audit trail, robot navigation status and deterministic safety-gate state.

Review actions: ACCEPT, REJECT, UNKNOWN, REQUEST_MORE_DATA.

The UI must not contain an unrestricted AI-to-motor command path.
