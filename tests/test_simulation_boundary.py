import json
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("dry_run", ROOT / "simulation" / "dry_run.py")
dry_run = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dry_run)

def test_dry_run_never_emits_actuator_command():
    intent = dry_run.NavigationIntent("base_link", "STOP", 0.0, "test", "AUTHORIZED")
    payload = json.loads(dry_run.emit_dry_run(intent))
    assert payload["mode"] == "DRY_RUN"
    assert "actuator_command" not in payload

def test_dry_run_rejects_unauthorized_state():
    intent = dry_run.NavigationIntent("base_link", "FORWARD", 0.1, "test", "UNAUTHORIZED")
    try:
        dry_run.emit_dry_run(intent)
    except ValueError:
        return
    raise AssertionError("unauthorized intent was accepted")
