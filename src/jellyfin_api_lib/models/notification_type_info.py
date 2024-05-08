import builtins
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotificationTypeInfo")


@_attrs_define
class NotificationTypeInfo:
    """
    Attributes:
        type (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
        enabled (Union[Unset, bool]):
        category (Union[None, Unset, str]):
        is_based_on_user_event (Union[Unset, bool]):
    """

    type: None | Unset | str = UNSET
    name: None | Unset | str = UNSET
    enabled: Unset | bool = UNSET
    category: None | Unset | str = UNSET
    is_based_on_user_event: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        type: None | Unset | str
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        enabled = self.enabled

        category: None | Unset | str
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        is_based_on_user_event = self.is_based_on_user_event

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if name is not UNSET:
            field_dict["Name"] = name
        if enabled is not UNSET:
            field_dict["Enabled"] = enabled
        if category is not UNSET:
            field_dict["Category"] = category
        if is_based_on_user_event is not UNSET:
            field_dict["IsBasedOnUserEvent"] = is_based_on_user_event

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("Name", UNSET))

        enabled = d.pop("Enabled", UNSET)

        def _parse_category(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        category = _parse_category(d.pop("Category", UNSET))

        is_based_on_user_event = d.pop("IsBasedOnUserEvent", UNSET)

        notification_type_info = cls(
            type=type,
            name=name,
            enabled=enabled,
            category=category,
            is_based_on_user_event=is_based_on_user_event,
        )

        return notification_type_info
