from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="JoinGroupRequestDto")


@_attrs_define
class JoinGroupRequestDto:
    """Class JoinGroupRequestDto.

    Attributes:
        group_id (Union[Unset, str]): Gets or sets the group identifier.
    """

    group_id: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        group_id = self.group_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["GroupId"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("GroupId", UNSET)

        join_group_request_dto = cls(
            group_id=group_id,
        )

        return join_group_request_dto
