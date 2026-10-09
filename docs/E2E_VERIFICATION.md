# End-to-End Verification

## Purpose

The reference verifier independently checks that a pipeline result and its audit record agree, the evidence identifier matches the recorded evidence payload, confidence and counts are well-formed, abstention preserves UNKNOWN, human review remains mandatory, and the screening pipeline has not authorized robot motion.

## Run verification

```bash
python -m pip install -e '.[dev]'
pytest -q
```

## Use the verifier

```python
from pui89_e2e import EndToEndScreeningPipeline, SensorObservation, verify_pipeline_result

observations = [
    SensorObservation(
        sensor_id="camera-01",
        modality="rgb",
        timestamp="2026-10-09T10:00:00+00:00",
        quality=0.92,
    ),
    SensorObservation(
        sensor_id="depth-01",
        modality="depth",
        timestamp="2026-10-09T10:00:00+00:00",
        quality=0.95,
    ),
]
result = EndToEndScreeningPipeline().run(observations, case_id="demo-001")
report = verify_pipeline_result(result)

print(report.valid)
print(report.to_dict())
```

## What is checked

- Evidence ID recomputation against the evidence payload.
- Agreement between result fields and audit-record fields.
- Mandatory human review and a false robot-motion-authorization flag.
- Nonnegative observation counts and confidence within [0, 1].
- Only recognized pipeline states (`HUMAN_REVIEW` and `ABSTAIN`).
- `ABSTAIN` must preserve `unknown_substance` with zero confidence.

The automated tests include valid records, modified/tampered evidence, unsafe motion authorization, missing human review, and invalid abstention behavior.

## Security limitations

The evidence ID uses a truncated, unkeyed SHA-256 digest for consistency/tamper detection. It is **not a digital signature**, does not authenticate a reviewer or device, and is not sufficient against a malicious actor who can rewrite the record and recompute the digest. Production deployments should use access-controlled append-only storage, authenticated identities, signed records using managed keys, trusted timestamps, key rotation, and an independently reviewed threat model.

Passing these checks means only that these software-level consistency and safety invariants passed. It does not validate sensor accuracy, prove a substance's chemical identity, certify the robot, or replace human/forensic verification using appropriate validated procedures.
