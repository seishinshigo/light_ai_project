from app.style_registry import load_style, to_system_prompt

def test_prompt_conversion():
    style = load_style()
    prompt = to_system_prompt(style)
    assert "Style ID:" in prompt
    assert "Components:" in prompt
