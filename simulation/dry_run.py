from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class NavigationIntent:
    frame: str
    direction: str
    speed_limit: float
    reason: str
    safety_state: str

def emit_dry_run(intent: NavigationIntent) -> str:
    if intent.speed_limit < 0:
        raise ValueError("speed_limit must be non-negative")
    if intent.safety_state != "AUTHORIZED":
        raise ValueError("dry-run intent requires explicit authorized safety state")
    return json.dumps({"mode": "DRY_RUN", "intent": asdict(intent)}, sort_keys=True)

if __name__ == "__main__":
    print(emit_dry_run(NavigationIntent("base_link", "STOP", 0.0, "demo", "AUTHORIZED")))
