import builtins
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.external_id_media_type import ExternalIdMediaType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalIdInfo")


@_attrs_define
class ExternalIdInfo:
    """Represents the external id information for serialization to the client.

    Attributes:
        name (Union[Unset, str]): Gets or sets the display name of the external id provider (IE: IMDB, MusicBrainz,
            etc).
        key (Union[Unset, str]): Gets or sets the unique key for this id. This key should be unique across all
            providers.
        type (Union[ExternalIdMediaType, None, Unset]): Gets or sets the specific media type for this id. This is used
            to distinguish between the different
            external id types for providers with multiple ids.
            A null value indicates there is no specific media type associated with the external id, or this is the
            default id for the external provider so there is no need to specify a type.
        url_format_string (Union[None, Unset, str]): Gets or sets the URL format string.
    """

    name: Unset | str = UNSET
    key: Unset | str = UNSET
    type: ExternalIdMediaType | None | Unset = UNSET
    url_format_string: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        key = self.key

        type: None | Unset | str
        if isinstance(self.type, Unset):
            type = UNSET
        elif isinstance(self.type, ExternalIdMediaType):
            type = self.type.value
        else:
            type = self.type

        url_format_string: None | Unset | str
        if isinstance(self.url_format_string, Unset):
            url_format_string = UNSET
        else:
            url_format_string = self.url_format_string

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if key is not UNSET:
            field_dict["Key"] = key
        if type is not UNSET:
            field_dict["Type"] = type
        if url_format_string is not UNSET:
            field_dict["UrlFormatString"] = url_format_string

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        key = d.pop("Key", UNSET)

        def _parse_type(data: object) -> ExternalIdMediaType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_1 = ExternalIdMediaType(data)

                return type_type_1
            except:  # noqa: E722
                pass
            return cast(ExternalIdMediaType | None | Unset, data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_url_format_string(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        url_format_string = _parse_url_format_string(d.pop("UrlFormatString", UNSET))

        external_id_info = cls(
            name=name,
            key=key,
            type=type,
            url_format_string=url_format_string,
        )

        return external_id_info
