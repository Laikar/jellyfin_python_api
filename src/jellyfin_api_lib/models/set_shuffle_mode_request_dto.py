from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.group_shuffle_mode import GroupShuffleMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetShuffleModeRequestDto")


@_attrs_define
class SetShuffleModeRequestDto:
    """Class SetShuffleModeRequestDto.

    Attributes:
        mode (Union[Unset, GroupShuffleMode]): Enum GroupShuffleMode.
    """

    mode: Unset | GroupShuffleMode = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode: Unset | str = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if mode is not UNSET:
            field_dict["Mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _mode = d.pop("Mode", UNSET)
        mode: Unset | GroupShuffleMode
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = GroupShuffleMode(_mode)

        set_shuffle_mode_request_dto = cls(
            mode=mode,
        )

        return set_shuffle_mode_request_dto
