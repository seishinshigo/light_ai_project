#!/usr/bin/env python
from app.style_registry import load_style, to_system_prompt
import sys, pathlib

style = load_style()
prompt = to_system_prompt(style)
out = pathlib.Path("input/system_prompt.gemini")
out.write_text(prompt, encoding="utf-8")
print(f"Generated: {out}")
