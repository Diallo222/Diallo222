#!/usr/bin/env python3
from pathlib import Path

path = Path("dist/github-snake-green-dark.svg")
if not path.exists():
    raise SystemExit(f"Missing snake SVG: {path}")

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
