from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MediaEncoderPathDto")


@_attrs_define
class MediaEncoderPathDto:
    """Media Encoder Path Dto.

    Attributes:
        path (Union[Unset, str]): Gets or sets media encoder path.
        path_type (Union[Unset, str]): Gets or sets media encoder path type.
    """

    path: Unset | str = UNSET
    path_type: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        path_type = self.path_type

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if path is not UNSET:
            field_dict["Path"] = path
        if path_type is not UNSET:
            field_dict["PathType"] = path_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        path = d.pop("Path", UNSET)

        path_type = d.pop("PathType", UNSET)

        media_encoder_path_dto = cls(
            path=path,
            path_type=path_type,
        )

        return media_encoder_path_dto
