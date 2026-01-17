from ui.app import (
    UserMessage,
    AssistantMessage,
    ChatInput,
)
from ui.core import daisy_app


app, rt = daisy_app()


@rt
def msg(user_msg: str): ...
