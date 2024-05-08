from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="NextItemRequestDto")


@_attrs_define
class NextItemRequestDto:
    """Class NextItemRequestDto.

    Attributes:
        playlist_item_id (Union[Unset, str]): Gets or sets the playing item identifier.
    """

    playlist_item_id: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        playlist_item_id = self.playlist_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if playlist_item_id is not UNSET:
            field_dict["PlaylistItemId"] = playlist_item_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        playlist_item_id = d.pop("PlaylistItemId", UNSET)

        next_item_request_dto = cls(
            playlist_item_id=playlist_item_id,
        )

        return next_item_request_dto
