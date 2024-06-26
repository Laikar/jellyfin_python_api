from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaPathInfo")


@_attrs_define
class MediaPathInfo:
    """
    Attributes:
        path (Union[Unset, str]):
        network_path (Union[None, Unset, str]):
    """

    path: Unset | str = UNSET
    network_path: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        network_path: None | Unset | str
        if isinstance(self.network_path, Unset):
            network_path = UNSET
        else:
            network_path = self.network_path

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if network_path is not UNSET:
            field_dict["NetworkPath"] = network_path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("Path", UNSET)

        def _parse_network_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        network_path = _parse_network_path(d.pop("NetworkPath", UNSET))

        media_path_info = cls(
            path=path,
            network_path=network_path,
        )

        return media_path_info
