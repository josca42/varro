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
from .auth import (
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
    "UserMessage",
    "AssistantMessage",
    "ThinkingSteps",
    "EditsIndicator",
    "ChatInput",
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
