# Sensor Failure and Degraded Modes

The platform must degrade explicitly rather than silently pretending all modalities are available.

Full sensors -> quality gate -> normal fusion
Degraded sensor -> reduced confidence + human review
Missing modality -> provenance + degraded mode
No trustworthy perception -> abstain / stop screening

Missing sensors must be recorded in the evidence record. A missing modality must never be interpreted as negative evidence.
