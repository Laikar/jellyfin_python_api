from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="BasePluginConfiguration")


@_attrs_define
class BasePluginConfiguration:
    """Class BasePluginConfiguration."""

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        base_plugin_configuration = cls()

        return base_plugin_configuration
