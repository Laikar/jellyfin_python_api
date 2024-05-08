from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.playstate_command import PlaystateCommand
from ..types import UNSET, Unset

T = TypeVar("T", bound="PlaystateRequest")


@_attrs_define
class PlaystateRequest:
    """
    Attributes:
        command (Union[Unset, PlaystateCommand]): Enum PlaystateCommand.
        seek_position_ticks (Union[None, Unset, int]):
        controlling_user_id (Union[None, Unset, str]): Gets or sets the controlling user identifier.
    """

    command: Unset | PlaystateCommand = UNSET
    seek_position_ticks: None | Unset | int = UNSET
    controlling_user_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        command: Unset | str = UNSET
        if not isinstance(self.command, Unset):
            command = self.command.value

        seek_position_ticks: None | Unset | int
        if isinstance(self.seek_position_ticks, Unset):
            seek_position_ticks = UNSET
        else:
            seek_position_ticks = self.seek_position_ticks

        controlling_user_id: None | Unset | str
        if isinstance(self.controlling_user_id, Unset):
            controlling_user_id = UNSET
        else:
            controlling_user_id = self.controlling_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if command is not UNSET:
            field_dict["Command"] = command
        if seek_position_ticks is not UNSET:
            field_dict["SeekPositionTicks"] = seek_position_ticks
        if controlling_user_id is not UNSET:
            field_dict["ControllingUserId"] = controlling_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _command = d.pop("Command", UNSET)
        command: Unset | PlaystateCommand
        if isinstance(_command, Unset):
            command = UNSET
        else:
            command = PlaystateCommand(_command)

        def _parse_seek_position_ticks(data: object) -> None | Unset | int:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | int, data)

        seek_position_ticks = _parse_seek_position_ticks(d.pop("SeekPositionTicks", UNSET))

        def _parse_controlling_user_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        controlling_user_id = _parse_controlling_user_id(d.pop("ControllingUserId", UNSET))

        playstate_request = cls(
            command=command,
            seek_position_ticks=seek_position_ticks,
            controlling_user_id=controlling_user_id,
        )

        return playstate_request
