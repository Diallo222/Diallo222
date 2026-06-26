#!/usr/bin/env python3
import sys
import traceback
from pathlib import Path

path = Path("dist/github-snake-lime.svg")
if not path.exists():
    candidates = list(Path("dist").glob("*lime*.svg"))
    if not candidates:
        print("dist contents:", list(Path("dist").glob("*")) if Path("dist").exists() else "missing dist/")
        raise SystemExit(f"Missing snake SVG: {path}")
    path = candidates[0]

try:
    text = path.read_text()
    replacements = {
        "var(--cs)": "#a3e635",
        "var(--ce)": "#21262d",
        "var(--c0)": "#21262d",
        "var(--c1)": "#0e4429",
        "var(--c2)": "#006d32",
        "var(--c3)": "#39d353",
        "var(--c4)": "#7ee787",
        "var(--cb)": "#1b1f230a",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    if "var(--" in text:
        raise SystemExit("Snake SVG still contains CSS variables after inlining")

    path.write_text(text)
    print(f"Inlined snake colors in {path}")
except Exception as exc:
    traceback.print_exc()
    raise SystemExit(str(exc)) from exc
