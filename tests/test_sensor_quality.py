from narcotics_platform.sensor_quality import SensorStatus, assess_sensor_quality

def test_sensor_quality_reports_degraded_modality():
    report = assess_sensor_quality({'rgb':SensorStatus('rgb',quality=0.9),'thermal':SensorStatus('thermal',quality=0.3)})
    assert 'thermal' in report.degraded_modalities
    assert report.usable
