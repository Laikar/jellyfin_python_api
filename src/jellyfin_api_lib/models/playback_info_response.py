from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.playback_error_code import PlaybackErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.media_source_info import MediaSourceInfo


T = TypeVar("T", bound="PlaybackInfoResponse")


@_attrs_define
class PlaybackInfoResponse:
    """Class PlaybackInfoResponse.

    Attributes:
        media_sources (Union[Unset, List['MediaSourceInfo']]): Gets or sets the media sources.
        play_session_id (Union[None, Unset, str]): Gets or sets the play session identifier.
        error_code (Union[None, PlaybackErrorCode, Unset]): Gets or sets the error code.
    """

    media_sources: Unset | list["MediaSourceInfo"] = UNSET
    play_session_id: None | Unset | str = UNSET
    error_code: None | PlaybackErrorCode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        media_sources: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.media_sources, Unset):
            media_sources = []
            for media_sources_item_data in self.media_sources:
                media_sources_item = media_sources_item_data.to_dict()
                media_sources.append(media_sources_item)

        play_session_id: None | Unset | str
        if isinstance(self.play_session_id, Unset):
            play_session_id = UNSET
        else:
            play_session_id = self.play_session_id

        error_code: None | Unset | str
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        elif isinstance(self.error_code, PlaybackErrorCode):
            error_code = self.error_code.value
        else:
            error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if media_sources is not UNSET:
            field_dict["MediaSources"] = media_sources
        if play_session_id is not UNSET:
            field_dict["PlaySessionId"] = play_session_id
        if error_code is not UNSET:
            field_dict["ErrorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.media_source_info import MediaSourceInfo

        d = src_dict.copy()
        media_sources = []
        _media_sources = d.pop("MediaSources", UNSET)
        for media_sources_item_data in _media_sources or []:
            media_sources_item = MediaSourceInfo.from_dict(media_sources_item_data)

            media_sources.append(media_sources_item)

        def _parse_play_session_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        play_session_id = _parse_play_session_id(d.pop("PlaySessionId", UNSET))

        def _parse_error_code(data: object) -> None | PlaybackErrorCode | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                error_code_type_1 = PlaybackErrorCode(data)

                return error_code_type_1
            except:  # noqa: E722
                pass
            return cast(None | PlaybackErrorCode | Unset, data)

        error_code = _parse_error_code(d.pop("ErrorCode", UNSET))

        playback_info_response = cls(
            media_sources=media_sources,
            play_session_id=play_session_id,
            error_code=error_code,
        )

        return playback_info_response
