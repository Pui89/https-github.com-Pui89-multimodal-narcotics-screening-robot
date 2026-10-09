from pui89_e2e import (
    EndToEndScreeningPipeline,
    SensorObservation,
    verify_pipeline_result,
)


T0 = "2026-10-09T10:00:00+00:00"


def obs(sensor_id, modality, *, quality=0.9, label="methamphetamine_crystal", confidence=0.9, timestamp=T0):
    return SensorObservation(
        sensor_id=sensor_id,
        modality=modality,
        timestamp=timestamp,
        quality=quality,
        candidate_label=label,
        confidence=confidence,
    )


def result_for(observations=None):
    return EndToEndScreeningPipeline().run(
        observations if observations is not None else [obs("cam-1", "rgb"), obs("depth-1", "depth")],
        case_id="verification-test",
        now=T0,
    )


def test_valid_result_passes_independent_verification():
    result = result_for()
    report = verify_pipeline_result(result)

    assert report.valid is True
    assert report.errors == []
    assert all(report.checks.values())
    assert report.evidence_id == result.evidence_id


def test_tampered_audit_hypothesis_fails_integrity_verification():
    result = result_for().to_dict()
    result["audit_record"]["hypothesis"] = "heroin"

    report = verify_pipeline_result(result)

    assert report.valid is False
    assert "evidence_id_integrity_check_failed" in report.errors


def test_verifier_rejects_motion_authorization():
    result = result_for().to_dict()
    result["robot_motion_authorized"] = True

    report = verify_pipeline_result(result)

    assert report.valid is False
    assert "robot_motion_must_not_be_authorized_by_screening_pipeline" in report.errors


def test_verifier_rejects_missing_human_review():
    result = result_for().to_dict()
    result["human_review_required"] = False

    report = verify_pipeline_result(result)

    assert report.valid is False
    assert "human_review_must_remain_required" in report.errors


def test_abstention_is_verified_only_when_unknown_is_preserved():
    result = result_for([obs("cam-1", "rgb", quality=0.1)])
    assert verify_pipeline_result(result).valid is True

    altered = result.to_dict()
    altered["screening_hypothesis"] = "heroin"
    report = verify_pipeline_result(altered)

    assert report.valid is False
    assert "hypothesis_matches" in report.errors
