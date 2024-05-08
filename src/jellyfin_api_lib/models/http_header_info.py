from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.header_match_type import HeaderMatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="HttpHeaderInfo")


@_attrs_define
class HttpHeaderInfo:
    """
    Attributes:
        name (Union[None, Unset, str]):
        value (Union[None, Unset, str]):
        match (Union[Unset, HeaderMatchType]):
    """

    name: None | Unset | str = UNSET
    value: None | Unset | str = UNSET
    match: Unset | HeaderMatchType = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        value: None | Unset | str
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        match: Unset | str = UNSET
        if not isinstance(self.match, Unset):
            match = self.match.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if value is not UNSET:
            field_dict["Value"] = value
        if match is not UNSET:
            field_dict["Match"] = match

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

        def _parse_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        value = _parse_value(d.pop("Value", UNSET))

        _match = d.pop("Match", UNSET)
        match: Unset | HeaderMatchType
        if isinstance(_match, Unset):
            match = UNSET
        else:
            match = HeaderMatchType(_match)

        http_header_info = cls(
            name=name,
            value=value,
            match=match,
        )

        return http_header_info
