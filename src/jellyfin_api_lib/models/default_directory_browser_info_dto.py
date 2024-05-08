from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DefaultDirectoryBrowserInfoDto")


@_attrs_define
class DefaultDirectoryBrowserInfoDto:
    """Default directory browser info.

    Attributes:
        path (Union[None, Unset, str]): Gets or sets the path.
    """

    path: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        path: None | Unset | str
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_path(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        path = _parse_path(d.pop("Path", UNSET))

        default_directory_browser_info_dto = cls(
            path=path,
        )

        return default_directory_browser_info_dto
