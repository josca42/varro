"""ui.app

App-specific UI compositions for this repository.

These are not general-purpose components; they implement the look and structure
used in `main.py`.
"""

from .navbar import Navbar
from .chat import (
    UserMessage,
    AssistantMessage,
    ThinkingSteps,
    EditsIndicator,
    ChatInput,
)
from .dashboard import (
    MetricCard,
    ChartShell,
    DashboardPanel,
)

__all__ = [
    "Navbar",
    # Chat
    "UserMessage",
    "AssistantMessage",
    "ThinkingSteps",
    "EditsIndicator",
    "ChatInput",
    # Dashboard
    "MetricCard",
    "ChartShell",
    "DashboardPanel",
]
