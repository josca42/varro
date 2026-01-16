"""dashboard.filters

Pydantic filter definitions and helpers.
"""

from __future__ import annotations

from typing import Any, Literal, Mapping

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


class Filter(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: str
    name: str
    label: str | None = None

    @field_validator("name")
    @classmethod
    def _name_required(cls, value: str) -> str:
        if not value or not value.strip():
            raise ValueError("filter name is required")
        return value

    @field_validator("label", mode="before")
    @classmethod
    def _default_label(cls, value: str | None, info) -> str | None:
        if value is None or value == "":
            return info.data.get("name") or None
        return value

    def parse_query_params(self, params: Mapping[str, str]) -> dict[str, Any]:
        raise NotImplementedError

    def url_params(self, filters: Mapping[str, Any]) -> dict[str, str]:
        raise NotImplementedError


class SelectFilter(Filter):
    type: Literal["select"]
    default: str = "all"
    options_query: str | None = None

    @field_validator("options_query", mode="before")
    @classmethod
    def _clean_options_query(cls, value: str | None) -> str | None:
        if value is None:
            return None
        if isinstance(value, str):
            value = value.strip()
        if not value:
            raise ValueError("options query cannot be empty")
        return value

    def parse_query_params(self, params: Mapping[str, str]) -> dict[str, Any]:
        value = params.get(self.name, self.default)
        return {self.name: value}

    def url_params(self, filters: Mapping[str, Any]) -> dict[str, str]:
        value = filters.get(self.name, self.default)
        if value != self.default:
            return {self.name: str(value)}
        return {}


class DateRangeFilter(Filter):
    type: Literal["daterange"]
    default: str = "all"
    default_from: str | None = None
    default_to: str | None = None

    @field_validator("default_from", "default_to", mode="before")
    @classmethod
    def _empty_to_none(cls, value: str | None) -> str | None:
        if value == "":
            return None
        return value

    @model_validator(mode="after")
    def _normalize_defaults(self) -> "DateRangeFilter":
        if self.default == "all":
            self.default_from = None
            self.default_to = None
        return self

    def parse_query_params(self, params: Mapping[str, str]) -> dict[str, Any]:
        from_key = f"{self.name}_from"
        to_key = f"{self.name}_to"
        from_val = params.get(from_key, self.default_from)
        to_val = params.get(to_key, self.default_to)
        return {
            from_key: from_val or None,
            to_key: to_val or None,
        }

    def url_params(self, filters: Mapping[str, Any]) -> dict[str, str]:
        from_key = f"{self.name}_from"
        to_key = f"{self.name}_to"
        from_val = filters.get(from_key) or ""
        to_val = filters.get(to_key) or ""
        default_from = self.default_from or ""
        default_to = self.default_to or ""
        params: dict[str, str] = {}
        if from_val and from_val != default_from:
            params[from_key] = from_val
        if to_val and to_val != default_to:
            params[to_key] = to_val
        return params


class CheckboxFilter(Filter):
    type: Literal["checkbox"]
    default: bool = False

    @field_validator("default", mode="before")
    @classmethod
    def _parse_default(cls, value: Any) -> bool:
        if isinstance(value, str):
            return value.lower() == "true"
        return bool(value)

    def parse_query_params(self, params: Mapping[str, str]) -> dict[str, Any]:
        value = params.get(self.name)
        if value is None:
            return {self.name: self.default}
        return {self.name: value.lower() == "true"}

    def url_params(self, filters: Mapping[str, Any]) -> dict[str, str]:
        value = filters.get(self.name, self.default)
        if value != self.default:
            return {self.name: "true" if value else "false"}
        return {}


def filter_from_component(type_: str, attrs: dict[str, str]) -> Filter | None:
    if type_ == "select":
        options_raw = (attrs.get("options") or "").strip()
        options_query = None
        if options_raw:
            if not options_raw.startswith("query:"):
                raise ValueError(
                    "select filter options must start with 'query:'"
                )
            options_query = options_raw.removeprefix("query:").strip()
        return SelectFilter(
            type="select",
            name=attrs.get("name", ""),
            label=attrs.get("label"),
            default=attrs.get("default", "all"),
            options_query=options_query,
        )

    if type_ == "daterange":
        return DateRangeFilter(
            type="daterange",
            name=attrs.get("name", ""),
            label=attrs.get("label"),
            default=attrs.get("default", "all"),
            default_from=attrs.get("default_from"),
            default_to=attrs.get("default_to"),
        )

    if type_ == "checkbox":
        return CheckboxFilter(
            type="checkbox",
            name=attrs.get("name", ""),
            label=attrs.get("label"),
            default=attrs.get("default", "false"),
        )

    return None


def validate_options_queries(
    filters: list[Filter],
    queries: dict[str, str],
) -> None:
    """Ensure select filters reference options queries that exist."""
    for f in filters:
        if isinstance(f, SelectFilter) and f.options_query:
            if f.options_query not in queries:
                raise ValueError(
                    f"Unknown options query '{f.options_query}' for filter '{f.name}'"
                )

