import builtins
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemDetails")


@_attrs_define
class ProblemDetails:
    """
    Attributes:
        type (Union[None, Unset, str]):
        title (Union[None, Unset, str]):
        status (Union[None, Unset, int]):
        detail (Union[None, Unset, str]):
        instance (Union[None, Unset, str]):
    """

    type: None | Unset | str = UNSET
    title: None | Unset | str = UNSET
    status: None | Unset | int = UNSET
    detail: None | Unset | str = UNSET
    instance: None | Unset | str = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type: None | Unset | str
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        title: None | Unset | str
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: None | Unset | int
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        detail: None | Unset | str
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: None | Unset | str
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance

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

        type = _parse_type(d.pop("type", UNSET))

        def _parse_title(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_detail(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_instance(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        instance = _parse_instance(d.pop("instance", UNSET))

        problem_details = cls(
            type=type,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
        )

        problem_details.additional_properties = d
        return problem_details

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
