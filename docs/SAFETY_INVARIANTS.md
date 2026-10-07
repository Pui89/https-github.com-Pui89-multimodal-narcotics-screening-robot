# Safety Invariants

These invariants are architectural requirements, not model preferences.

1. **No AI-to-motor direct path.** Foundation models cannot directly command actuators.
2. **Deterministic motion gate.** Every motion command passes collision, workspace and emergency-stop checks.
3. **Unknown is not a positive identification.** Unknown/OOD output cannot autonomously trigger enforcement.
4. **Sensor-confidence degradation is fail-safe.** Missing or unreliable sensors reduce autonomy rather than silently increasing confidence.
5. **Emergency stop dominates.** Emergency-stop state overrides every AI process.
6. **Human review for consequential screening.** The AI produces evidence and uncertainty for an authorized reviewer.
7. **Auditability.** Model version, sensor provenance, timestamps and reviewer outcome are retained according to the project's data-minimization policy.
8. **No unnecessary person identification.** The system should operate on accessible objects/surfaces and avoid unrelated biometric identification.
