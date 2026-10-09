from pui89_e2e import EndToEndScreeningPipeline, SensorObservation


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


def test_multimodal_flow_produces_reviewable_evidence_and_never_authorizes_motion():
    result = EndToEndScreeningPipeline().run(
        [obs("cam-1", "rgb"), obs("depth-1", "depth")],
        case_id="test-001",
        now=T0,
    )

    assert result.status == "HUMAN_REVIEW"
    assert result.screening_hypothesis == "methamphetamine_crystal"
    assert result.accepted_observations == 2
    assert set(result.modalities) == {"rgb", "depth"}
    assert result.human_review_required is True
    assert result.robot_motion_authorized is False
    assert result.evidence_id.startswith("ev-")
    assert result.audit_record["case_id"] == "test-001"
    assert "not chemical identification" in result.audit_record["disclaimer"]


def test_low_quality_inputs_are_rejected_and_pipeline_abstains():
    result = EndToEndScreeningPipeline().run(
        [obs("cam-1", "rgb", quality=0.1)],
        now=T0,
    )

    assert result.status == "ABSTAIN"
    assert result.screening_hypothesis == "unknown_substance"
    assert result.accepted_observations == 0
    assert result.rejected_observations == 1
    assert result.robot_motion_authorized is False


def test_temporally_misaligned_sensors_are_not_fused():
    result = EndToEndScreeningPipeline().run(
        [
            obs("cam-1", "rgb", timestamp=T0),
            obs("depth-1", "depth", timestamp="2026-10-09T10:00:10+00:00"),
        ],
        now=T0,
    )

    assert result.status == "ABSTAIN"
    assert result.accepted_observations == 0
    assert "temporal_alignment_failed" in result.reasons
    assert result.robot_motion_authorized is False


def test_single_modality_cannot_be_treated_as_multimodal_confirmation():
    result = EndToEndScreeningPipeline().run([obs("cam-1", "rgb")], now=T0)

    assert result.status == "HUMAN_REVIEW"
    assert "insufficient_independent_modalities" in result.reasons
    assert result.human_review_required is True
