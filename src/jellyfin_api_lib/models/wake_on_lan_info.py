from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="WakeOnLanInfo")


@_attrs_define
class WakeOnLanInfo:
    """Provides the MAC address and port for wake-on-LAN functionality.

    Attributes:
        mac_address (Union[None, Unset, str]): Gets the MAC address of the device.
        port (Union[Unset, int]): Gets or sets the wake-on-LAN port.
    """

    mac_address: None | Unset | str = UNSET
    port: Unset | int = UNSET

    def to_dict(self) -> dict[str, Any]:
        mac_address: None | Unset | str
        if isinstance(self.mac_address, Unset):
            mac_address = UNSET
        else:
            mac_address = self.mac_address

        port = self.port

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if mac_address is not UNSET:
            field_dict["MacAddress"] = mac_address
        if port is not UNSET:
            field_dict["Port"] = port

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_mac_address(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        mac_address = _parse_mac_address(d.pop("MacAddress", UNSET))

        port = d.pop("Port", UNSET)

        wake_on_lan_info = cls(
            mac_address=mac_address,
            port=port,
        )

        return wake_on_lan_info
