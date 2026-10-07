# Uncertainty, Calibration and Open-Set Design

## Motivation

A screening robot must be able to say **unknown** or **abstain**. A high softmax score is not evidence that an observation belongs to a known class.

## Proposed decision stack

1. Generate multimodal evidence.
2. Estimate predictive uncertainty.
3. Estimate out-of-distribution (OOD) likelihood.
4. Check modality availability and sensor quality.
5. Apply calibrated abstention thresholds.
6. Route consequential cases to human review.

## Candidate methods

Compare:

- temperature scaling
- deep ensembles
- MC dropout
- entropy-based uncertainty
- feature-space/OOD scoring
- conformal prediction
- disagreement across modalities

The final method should be selected empirically rather than assumed to be optimal.

## Example output schema

~~~text
screening_hypothesis: unknown
confidence: 0.71
uncertainty: 0.24
ood_score: 0.18
missing_modalities: ["thermal"]
decision: ABSTAIN_HUMAN_REVIEW
~~~

These values are an interface example, not measured results.

## Selective prediction

Report risk-coverage curves and compare models at matched coverage. The central safety question is not only "how accurate is the model?" but also "does it know when evidence is insufficient?"

## Safety rule

Unknown/OOD status must never autonomously trigger enforcement, restraint, seizure, or other consequential action.
