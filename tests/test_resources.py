"""The MCP comparison must render as Markdown in clients."""

from elementor_mcp_lite.__main__ import pro_features


def test_pro_comparison_has_real_markdown_lines():
    comparison = pro_features()
    lines = comparison.splitlines()
    assert lines[0] == "# Upgrade to Pro — Elementor MCP"
    assert "| Capability | Lite | Separate Pro product |" in lines
    assert len([line for line in lines if line.startswith("| ")]) == 7
    assert "\\n" not in comparison
