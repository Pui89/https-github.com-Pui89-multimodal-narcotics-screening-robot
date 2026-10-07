from dataclasses import dataclass

@dataclass(frozen=True)
class TelemetryPolicy:
    protocol: str = 'MQTT'
    compressed_video: bool = True
    retain_raw_video_by_default: bool = False
    redact_sensitive_metadata: bool = True

def build_alert(event: str, gps: tuple[float, float] | None = None) -> dict:
    payload = {'event': event}
    if gps is not None:
        payload['gps'] = {'lat': gps[0], 'lon': gps[1]}
    return payload
