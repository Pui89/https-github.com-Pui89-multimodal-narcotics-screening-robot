from narcotics_platform import DEFAULT_SCENARIOS, ModelLifecycle, ModelStage, Point3D, ReviewDecision, ReviewRecord, RuntimeMonitor, SpatialEvidence, TemporalEvidenceBuffer, TemporalObservation

def test_temporal_buffer():
    b=TemporalEvidenceBuffer(4)
    for i in range(3): b.add(TemporalObservation(i,"unknown_substance",0.8,0.2))
    assert b.stable_label()=="unknown_substance"

def test_geometry():
    e=SpatialEvidence(Point3D(1,2,3),(0.01,0.01,0.04),0.9,"map",1.0)
    assert 0 < e.quality() <= 1

def test_governance():
    m=ModelLifecycle("demo","1")
    for stage in (ModelStage.VALIDATION,ModelStage.CALIBRATION,ModelStage.SAFETY_REVIEW,ModelStage.APPROVED): m.transition(stage)
    assert m.deployment_allowed()

def test_review():
    ReviewRecord("evt",ReviewDecision.UNKNOWN,"reviewer","insufficient evidence","2026-01-01","a"*64).validate()

def test_monitoring():
    m=RuntimeMonitor(); m.record_frame(inference_ms=10); m.record_frame(inference_ms=0,dropped=True); m.record_decision(ood=True,abstained=True)
    assert m.snapshot()["frames_seen"]==1 and m.snapshot()["frames_dropped"]==1

def test_stress_catalog():
    ids={x.scenario_id for x in DEFAULT_SCENARIOS}
    assert {"ood","timestamp-skew","sensor-disagreement"} <= ids
