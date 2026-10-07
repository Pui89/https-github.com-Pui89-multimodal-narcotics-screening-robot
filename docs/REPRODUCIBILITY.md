# Reproducibility Protocol

## Required experiment record

Each experiment should record:

- git commit SHA
- configuration file
- dataset version and split
- preprocessing version
- model/checkpoint identifier
- random seeds
- hardware/software environment
- evaluation command
- metric outputs
- failure cases

## Recommended repository layout

~~~text
configs/
  baseline_rgb.yaml
  baseline_thermal.yaml
  baseline_fusion.yaml
  proposed_model.yaml
  sensor_dropout.yaml
benchmarks/
experiments/
results/
models/
src/
tests/
simulation/
paper/
docs/
~~~

## Dataset policy

Do not fabricate performance by inventing data. Until an authorized real dataset is available, use clearly labeled synthetic/simulation experiments and report them as such.

## Publication standard

A paper-ready result should be reproducible from a clean environment using versioned configuration and documented commands. Any unavailable proprietary component must be identified explicitly.

## Reproducibility checklist

- [ ] deterministic split
- [ ] baseline implementations
- [ ] ablation study
- [ ] stress tests
- [ ] calibration analysis
- [ ] open-set analysis
- [ ] confidence intervals
- [ ] failure-case analysis
- [ ] safety audit
- [ ] limitations
