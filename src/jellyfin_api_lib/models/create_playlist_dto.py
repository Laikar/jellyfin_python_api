from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreatePlaylistDto")


@_attrs_define
class CreatePlaylistDto:
    """Create new playlist dto.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name of the new playlist.
        ids (Union[Unset, List[str]]): Gets or sets item ids to add to the playlist.
        user_id (Union[None, Unset, str]): Gets or sets the user id.
        media_type (Union[None, Unset, str]): Gets or sets the media type.
    """

    name: None | Unset | str = UNSET
    ids: Unset | list[str] = UNSET
    user_id: None | Unset | str = UNSET
    media_type: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        ids: Unset | list[str] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        user_id: None | Unset | str
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        media_type: None | Unset | str
        if isinstance(self.media_type, Unset):
            media_type = UNSET
        else:
            media_type = self.media_type

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if ids is not UNSET:
            field_dict["Ids"] = ids
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if media_type is not UNSET:
            field_dict["MediaType"] = media_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("Name", UNSET))

        ids = cast(list[str], d.pop("Ids", UNSET))

        def _parse_user_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_id = _parse_user_id(d.pop("UserId", UNSET))

        def _parse_media_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        media_type = _parse_media_type(d.pop("MediaType", UNSET))

        create_playlist_dto = cls(
            name=name,
            ids=ids,
            user_id=user_id,
            media_type=media_type,
        )

        return create_playlist_dto
