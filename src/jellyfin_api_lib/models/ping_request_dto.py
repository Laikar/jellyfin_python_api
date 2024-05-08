from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PingRequestDto")


@_attrs_define
class PingRequestDto:
    """Class PingRequestDto.

    Attributes:
        ping (Union[Unset, int]): Gets or sets the ping time.
    """

    ping: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        ping = self.ping

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ping is not UNSET:
            field_dict["Ping"] = ping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ping = d.pop("Ping", UNSET)

        ping_request_dto = cls(
            ping=ping,
        )

        return ping_request_dto
