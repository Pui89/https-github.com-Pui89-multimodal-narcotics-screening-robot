# Deployment Checklist

Before connecting physical robotics hardware:

- [ ] Dataset and sensor permissions are documented.
- [ ] Sensor calibration and timestamp synchronization are verified.
- [ ] Sensor failure and missing-modality behavior is tested.
- [ ] Unknown/OOD abstention is tested.
- [ ] Confidence calibration is measured on a held-out validation set.
- [ ] Robustness scenarios are evaluated.
- [ ] Model versions and checksums are recorded.
- [ ] Evidence records contain provenance and reviewer state.
- [ ] Foundation models are isolated from actuator commands.
- [ ] Deterministic safety gate and emergency stop are verified.
- [ ] Navigation is tested in simulation/recorded data before hardware.
- [ ] Human-review workflow is available for consequential cases.
- [ ] Privacy/retention controls are enabled for deployment data.

A deployment is not validated merely because inference runs successfully. Validation requires reproducible evidence that the complete system behaves safely under expected and degraded conditions.
