"""ui.app

App-specific UI compositions for this repository.

These are not general-purpose components; they implement the look and structure
used in `main.py`.
"""

from ui.app.navbar import Navbar
from ui.app.chat import (
    ChatPage,
    ChatMessages,
    TurnComponent,
    ChatForm,
    ChatFormDisabled,
    ChatFormEnabled,
    UserMessage,
    UserPromptBlock,
    ModelRequestBlock,
    CallToolsBlock,
    ToolResultBlock,
    ThinkingBlock,
    ToolCallBlock,
    ToolArgsDisplay,
    ToolResultDisplay,
    TextBlock,
    ErrorBlock,
    ChatHeader,
    ChatDropdownTrigger,
    ChatDropdown,
    ChatDropdownItem,
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

__all__ = [
    "Navbar",
    # Chat
    "ChatPage",
    "ChatMessages",
    "TurnComponent",
    "ChatForm",
    "ChatFormDisabled",
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
    "ChatHeader",
    "ChatDropdownTrigger",
    "ChatDropdown",
    "ChatDropdownItem",
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
]
