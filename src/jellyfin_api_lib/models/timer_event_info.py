from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimerEventInfo")


@_attrs_define
class TimerEventInfo:
    """
    Attributes:
        id (Union[Unset, str]):
        program_id (Union[None, Unset, str]):
    """

    id: Unset | str = UNSET
    program_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        program_id: None | Unset | str
        if isinstance(self.program_id, Unset):
            program_id = UNSET
        else:
            program_id = self.program_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if program_id is not UNSET:
            field_dict["ProgramId"] = program_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_program_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        program_id = _parse_program_id(d.pop("ProgramId", UNSET))

        timer_event_info = cls(
            id=id,
            program_id=program_id,
        )

        return timer_event_info
