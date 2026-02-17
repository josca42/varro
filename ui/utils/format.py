"""ui.utils.format

Number and value formatting utilities.
"""

from __future__ import annotations


def abbrev(n: float | int) -> str:
    """Abbreviate large numbers with K/M/B suffixes."""
    if abs(n) >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    if abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if abs(n) >= 1_000:
        return f"{n / 1_000:.1f}K"
    return f"{n:,.0f}"


def format_value(value: float | int | str, fmt: str) -> str:
    """Format a value according to format type.

    Args:
        value: The value to format
        fmt: Format type - "currency", "percent", or "number"
    """
    if isinstance(value, str):
        return value
    if fmt == "currency":
        return f"{abbrev(value)} kr."
    if fmt == "percent":
        return f"{value:.1%}"
    return abbrev(value)

