import builtins
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TunerHostInfo")


@_attrs_define
class TunerHostInfo:
    """
    Attributes:
        id (Union[None, Unset, str]):
        url (Union[None, Unset, str]):
        type (Union[None, Unset, str]):
        device_id (Union[None, Unset, str]):
        friendly_name (Union[None, Unset, str]):
        import_favorites_only (Union[Unset, bool]):
        allow_hw_transcoding (Union[Unset, bool]):
        enable_stream_looping (Union[Unset, bool]):
        source (Union[None, Unset, str]):
        tuner_count (Union[Unset, int]):
        user_agent (Union[None, Unset, str]):
    """

    id: None | Unset | str = UNSET
    url: None | Unset | str = UNSET
    type: None | Unset | str = UNSET
    device_id: None | Unset | str = UNSET
    friendly_name: None | Unset | str = UNSET
    import_favorites_only: Unset | bool = UNSET
    allow_hw_transcoding: Unset | bool = UNSET
    enable_stream_looping: Unset | bool = UNSET
    source: None | Unset | str = UNSET
    tuner_count: Unset | int = UNSET
    user_agent: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | Unset | str
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        url: None | Unset | str
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        type: None | Unset | str
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        device_id: None | Unset | str
        if isinstance(self.device_id, Unset):
            device_id = UNSET
        else:
            device_id = self.device_id

        friendly_name: None | Unset | str
        if isinstance(self.friendly_name, Unset):
            friendly_name = UNSET
        else:
            friendly_name = self.friendly_name

        import_favorites_only = self.import_favorites_only

        allow_hw_transcoding = self.allow_hw_transcoding

        enable_stream_looping = self.enable_stream_looping

        source: None | Unset | str
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        tuner_count = self.tuner_count

        user_agent: None | Unset | str
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["Id"] = id
        if url is not UNSET:
            field_dict["Url"] = url
        if type is not UNSET:
            field_dict["Type"] = type
        if device_id is not UNSET:
            field_dict["DeviceId"] = device_id
        if friendly_name is not UNSET:
            field_dict["FriendlyName"] = friendly_name
        if import_favorites_only is not UNSET:
            field_dict["ImportFavoritesOnly"] = import_favorites_only
        if allow_hw_transcoding is not UNSET:
            field_dict["AllowHWTranscoding"] = allow_hw_transcoding
        if enable_stream_looping is not UNSET:
            field_dict["EnableStreamLooping"] = enable_stream_looping
        if source is not UNSET:
            field_dict["Source"] = source
        if tuner_count is not UNSET:
            field_dict["TunerCount"] = tuner_count
        if user_agent is not UNSET:
            field_dict["UserAgent"] = user_agent

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        id = _parse_id(d.pop("Id", UNSET))

        def _parse_url(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        url = _parse_url(d.pop("Url", UNSET))

        def _parse_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_device_id(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        device_id = _parse_device_id(d.pop("DeviceId", UNSET))

        def _parse_friendly_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        friendly_name = _parse_friendly_name(d.pop("FriendlyName", UNSET))

        import_favorites_only = d.pop("ImportFavoritesOnly", UNSET)

        allow_hw_transcoding = d.pop("AllowHWTranscoding", UNSET)

        enable_stream_looping = d.pop("EnableStreamLooping", UNSET)

        def _parse_source(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        source = _parse_source(d.pop("Source", UNSET))

        tuner_count = d.pop("TunerCount", UNSET)

        def _parse_user_agent(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_agent = _parse_user_agent(d.pop("UserAgent", UNSET))

        tuner_host_info = cls(
            id=id,
            url=url,
            type=type,
            device_id=device_id,
            friendly_name=friendly_name,
            import_favorites_only=import_favorites_only,
            allow_hw_transcoding=allow_hw_transcoding,
            enable_stream_looping=enable_stream_looping,
            source=source,
            tuner_count=tuner_count,
            user_agent=user_agent,
        )

        return tuner_host_info
