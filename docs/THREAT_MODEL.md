# Threat Model

## Scope

The threat model covers a multimodal mobile robot that collects external sensor observations and produces screening hypotheses.

| Threat | Vulnerability | Mitigation | Residual risk |
|---|---|---|---|
| Sensor obstruction | Camera/LiDAR blocked | quality gate + confidence drop | degraded perception |
| Adversarial visual pattern | perception manipulation | cross-modal disagreement + OOD | novel attacks |
| Thermal/LiDAR interference | corrupted modality | modality health checks | partial observability |
| Data poisoning | contaminated training data | provenance, review, held-out tests | unknown contamination |
| Model manipulation | altered checkpoint/config | hashes, version pinning, access control | supply-chain risk |
| Network compromise | telemetry/control channel | authentication, segmentation, least privilege | residual cyber risk |
| Unauthorized operator | misuse | authorization + audit logs | insider risk |
| False evidence | model hallucination | evidence-grounded outputs + human review | reviewer error |

## Security principle

A foundation model may summarize or reason over evidence, but it must not become the sole trust boundary for safety-critical actuation or consequential screening.
