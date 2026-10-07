# Edge deployment

Target deployment split:

- Jetson Orin Nano: perception, segmentation, VLM inference, 3D fusion
- Raspberry Pi 5: telemetry, watchdog and auxiliary services
- robot controller: deterministic low-level control and E-stop

Cloud connectivity is optional. Safety and emergency-stop behavior must remain local.
