"""ui.app

App-specific UI compositions for this repository.

These are not general-purpose components; they implement the look and structure
used in `main.py`.
"""

from ui.app.navbar import Navbar
from ui.app.chat import (
    ChatPage,
    ChatPanel,
    ChatMessages,
    TurnComponent,
    ChatForm,
    ChatFormRunning,
    ChatFormEnabled,
    UserMessage,
    UserPromptBlock,
    ModelRequestBlock,
    CallToolsBlock,
    TextBlock,
    ErrorBlock,
    ChatHeader,
    ChatDropdownTrigger,
    ChatDropdown,
    ChatDropdownItem,
)
from ui.app.layout import (
    AppShell,
    DashboardOverviewPage,
    WelcomePage,
    OverviewPage,
    SettingsPage,
)
from ui.app.command_palette import CommandPalette, CommandPaletteScript
from ui.app.tool import (
    ThinkingBlock,
    ToolCallBlock,
    ToolResultBlock,
    ToolArgsDisplay,
    ToolResultDisplay,
    ReasoningBlock,
)
from ui.app.auth import (
    AuthPage,
    AuthFormCard,
    AuthSimpleCard,
    AuthNotices,
    AuthLinks,
    AuthGoogleCta,
    AuthLoginForm,
    AuthSignupForm,
    AuthVerificationResendForm,
    AuthPasswordResetForm,
    AuthPasswordResetConfirmForm,
)
from ui.app.frontpage import Frontpage

__all__ = [
    "Navbar",
    # Chat
    "ChatPage",
    "ChatPanel",
    "ChatMessages",
    "TurnComponent",
    "ChatForm",
    "ChatFormRunning",
    "ChatFormEnabled",
    "UserMessage",
    "UserPromptBlock",
    "ModelRequestBlock",
    "CallToolsBlock",
    "ToolResultBlock",
    "ThinkingBlock",
    "ToolCallBlock",
    "ToolArgsDisplay",
    "ToolResultDisplay",
    "TextBlock",
    "ErrorBlock",
    "ReasoningBlock",
    "ChatHeader",
    "ChatDropdownTrigger",
    "ChatDropdown",
    "ChatDropdownItem",
    # Layout
    "AppShell",
    "CommandPalette",
    "CommandPaletteScript",
    "DashboardOverviewPage",

    "WelcomePage",
    "OverviewPage",
    "SettingsPage",
    # Dashboard
    "MetricCard",
    "ChartShell",
    "DashboardPanel",
    # Auth
    "AuthPage",
    "AuthFormCard",
    "AuthSimpleCard",
    "AuthNotices",
    "AuthLinks",
    "AuthGoogleCta",
    "AuthLoginForm",
    "AuthSignupForm",
    "AuthVerificationResendForm",
    "AuthPasswordResetForm",
    "AuthPasswordResetConfirmForm",
    "Frontpage",
]
