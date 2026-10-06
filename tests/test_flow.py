from narcotics_platform.flow import EnvironmentalFlowEstimator

def test_flow_estimator():
    r = EnvironmentalFlowEstimator().estimate(2.5, 4.0)
    assert r.mean_speed_px_per_frame == 2.5
    assert r.rising_level_px == 4.0
