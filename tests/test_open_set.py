from narcotics_platform.open_set import classify_open_set

def test_low_confidence_abstains():
    decision = classify_open_set('heroin',0.42,0.1)
    assert decision.abstain
    assert decision.label == 'unknown_substance'

def test_high_ood_abstains():
    assert classify_open_set('heroin',0.9,0.8).abstain
