from narcotics_platform.fusion import ModalityEvidence, MultimodalFusion

def test_fusion_prefers_multi_modal_agreement():
    result = MultimodalFusion().fuse([ModalityEvidence('rgb','amphetamine',0.8), ModalityEvidence('depth','amphetamine',0.7), ModalityEvidence('thermal','unknown_substance',0.3)])
    assert result.label == 'amphetamine'
    assert result.agreement > 0.5
