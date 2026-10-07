from narcotics_platform.uncertainty import estimate_uncertainty

def test_degraded_inputs_increase_uncertainty():
    good = estimate_uncertainty(0.9,1.0,1.0,0.0)
    degraded = estimate_uncertainty(0.9,0.5,0.4,0.7)
    assert degraded.uncertainty > good.uncertainty
