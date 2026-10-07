# API contract

| Method | Path | Purpose |
|---|---|---|
| POST | /screen | submit authorized external-object/environment observations |
| GET | /health | service and actuator-boundary health |
| GET | /metrics | runtime metrics |
| GET | /models | approved model registry metadata |
| GET | /events/{id} | retrieve evidence event |
| POST | /review | record human-review decision |

No endpoint may accept arbitrary actuator commands. Robot motion remains in a separate ROS 2 navigation stack behind a deterministic safety gate.
