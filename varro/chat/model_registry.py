from __future__ import annotations

from dataclasses import dataclass
from typing import Any


DEFAULT_CHAT_MODEL_KEY = "anthropic_opus"

_ANTHROPIC_MODEL_SETTINGS = {
    "max_tokens": 16000,
    "anthropic_thinking": {"type": "adaptive"},
    "parallel_tool_calls": True,
    "anthropic_cache_instructions": "1h",
    "anthropic_cache_tool_definitions": "1h",
    "anthropic_cache_messages": "5m",
}

_GOOGLE_MODEL_SETTINGS = {
    "max_tokens": 16000,
}


@dataclass(frozen=True)
class ChatModel:
    key: str
    label: str
    provider_model_name: str
    billing_model_name: str
    model_settings: dict[str, Any]


CHAT_MODELS = (
    ChatModel(
        key="anthropic_opus",
        label="Claude Opus 4.6",
        provider_model_name="anthropic:claude-opus-4-6",
        billing_model_name="claude-opus-4-6",
        model_settings=_ANTHROPIC_MODEL_SETTINGS,
    ),
    ChatModel(
        key="anthropic_sonnet",
        label="Claude Sonnet 4.6",
        provider_model_name="anthropic:claude-sonnet-4-6",
        billing_model_name="claude-sonnet-4-6",
        model_settings=_ANTHROPIC_MODEL_SETTINGS,
    ),
    ChatModel(
        key="gemini_pro",
        label="Gemini 3.1 Pro Preview",
        provider_model_name="google-gla:gemini-3.1-pro-preview",
        billing_model_name="gemini-3.1-pro-preview",
        model_settings=_GOOGLE_MODEL_SETTINGS,
    ),
    ChatModel(
        key="gemini_flash",
        label="Gemini 3 Flash Preview",
        provider_model_name="google-gla:gemini-3-flash-preview",
        billing_model_name="gemini-3-flash-preview",
        model_settings=_GOOGLE_MODEL_SETTINGS,
    ),
)

CHAT_MODEL_BY_KEY = {model.key: model for model in CHAT_MODELS}


def all_chat_models() -> tuple[ChatModel, ...]:
    return CHAT_MODELS


def get_chat_model(key: str | None) -> ChatModel:
    if not key:
        return CHAT_MODEL_BY_KEY[DEFAULT_CHAT_MODEL_KEY]
    model = CHAT_MODEL_BY_KEY.get(key)
    if model is None:
        raise ValueError(f"Unknown chat model: {key}")
    return model
