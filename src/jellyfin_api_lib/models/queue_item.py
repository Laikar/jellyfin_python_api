from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueItem")


@_attrs_define
class QueueItem:
    """
    Attributes:
        id (Union[Unset, str]):
        playlist_item_id (Union[None, Unset, str]):
    """

    id: Unset | str = UNSET
    playlist_item_id: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        playlist_item_id: None | Unset | str
        if isinstance(self.playlist_item_id, Unset):
            playlist_item_id = UNSET
        else:
            playlist_item_id = self.playlist_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("Id", UNSET)

        def _parse_playlist_item_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        playlist_item_id = _parse_playlist_item_id(d.pop("PlaylistItemId", UNSET))

        queue_item = cls(
            id=id,
            playlist_item_id=playlist_item_id,
        )

        return queue_item
