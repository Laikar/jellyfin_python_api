from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryOptionInfoDto")


@_attrs_define
class LibraryOptionInfoDto:
    """Library option info dto.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets name.
        default_enabled (Union[Unset, bool]): Gets or sets a value indicating whether default enabled.
    """

    name: None | Unset | str = UNSET
    default_enabled: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        default_enabled = self.default_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if default_enabled is not UNSET:
            field_dict["DefaultEnabled"] = default_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("Name", UNSET))

        default_enabled = d.pop("DefaultEnabled", UNSET)

        library_option_info_dto = cls(
            name=name,
            default_enabled=default_enabled,
        )

        return library_option_info_dto
