import json, os
from pathlib import Path

REG_PATH = Path("data/dnd_style_registry.json")

def load_style(style_id="seishin_prm_v1") -> dict:
    with open(REG_PATH, encoding="utf-8") as f:
        data = json.load(f)
    if data["style_id"] != style_id:
        raise ValueError("Style ID not found")
    return data

def to_system_prompt(style: dict) -> str:
    comp = style["components"]
    prm = style["prm"]
    lines = [
        f"# Style ID: {style['style_id']}",
        "## Poetic Resonance Model:",
        ", ".join(prm["features"]),
        "## Components:"
    ]
    for k, v in comp.items():
        lines.append(f"- **{k}**: {v.get('tone','')}")
        for sub in v.values():
            if isinstance(sub, list):
                lines.append("  - " + ", ".join(sub))
    return "\n".join(lines)
