from narcotics_platform.safety import NavigationState, SafetyGate

def test_safe_motion():
    assert SafetyGate().allow_motion(NavigationState(0.95, 2.0))

def test_low_localization_blocks():
    assert not SafetyGate().allow_motion(NavigationState(0.50, 2.0))

def test_human_and_estop_block():
    g = SafetyGate()
    assert not g.allow_motion(NavigationState(0.95, 2.0, human_in_exclusion_zone=True))
    assert not g.allow_motion(NavigationState(0.95, 2.0, emergency_stop=True))
