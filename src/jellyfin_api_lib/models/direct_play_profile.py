import builtins
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DirectPlayProfile")


@_attrs_define
class DirectPlayProfile:
    """
    Attributes:
        container (Union[None, Unset, str]):
        audio_codec (Union[None, Unset, str]):
        video_codec (Union[None, Unset, str]):
        type (Union[Unset, DlnaProfileType]):
    """

    container: None | Unset | str = UNSET
    audio_codec: None | Unset | str = UNSET
    video_codec: None | Unset | str = UNSET
    type: Unset | DlnaProfileType = UNSET

    def to_dict(self) -> dict[str, Any]:
        container: None | Unset | str
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        audio_codec: None | Unset | str
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        video_codec: None | Unset | str
        if isinstance(self.video_codec, Unset):
            video_codec = UNSET
        else:
            video_codec = self.video_codec

        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if container is not UNSET:
            field_dict["Container"] = container
        if audio_codec is not UNSET:
            field_dict["AudioCodec"] = audio_codec
        if video_codec is not UNSET:
            field_dict["VideoCodec"] = video_codec
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_container(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        container = _parse_container(d.pop("Container", UNSET))

        def _parse_audio_codec(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        audio_codec = _parse_audio_codec(d.pop("AudioCodec", UNSET))

        def _parse_video_codec(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        video_codec = _parse_video_codec(d.pop("VideoCodec", UNSET))

        _type = d.pop("Type", UNSET)
        type: Unset | DlnaProfileType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DlnaProfileType(_type)

        direct_play_profile = cls(
            container=container,
            audio_codec=audio_codec,
            video_codec=video_codec,
            type=type,
        )

        return direct_play_profile
