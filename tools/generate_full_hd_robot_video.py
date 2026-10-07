#!/usr/bin/env python3
"""Create a 1920x1080 concept MP4 from the robot SVG using ImageMagick + FFmpeg.

This is a visualization asset generator, not a robotics-control program.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "docs" / "multimodal_narcotics_screening_robot_full_hd.svg"
OUT = ROOT / "docs" / "multimodal_narcotics_screening_robot_full_hd.mp4"
PNG = ROOT / "docs" / "_robot_frame.png"

subprocess.run(["magick", str(SVG), "-resize", "1920x1080!", str(PNG)], check=True)
subprocess.run([
    "ffmpeg", "-y", "-loop", "1", "-i", str(PNG),
    "-t", "8", "-r", "24", "-vf", "format=yuv420p",
    "-c:v", "libx264", "-movflags", "+faststart", str(OUT)
], check=True)
PNG.unlink(missing_ok=True)
print(OUT)
