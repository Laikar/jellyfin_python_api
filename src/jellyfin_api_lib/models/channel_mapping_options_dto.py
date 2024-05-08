from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.name_id_pair import NameIdPair
    from ..models.name_value_pair import NameValuePair
    from ..models.tuner_channel_mapping import TunerChannelMapping


T = TypeVar("T", bound="ChannelMappingOptionsDto")


@_attrs_define
class ChannelMappingOptionsDto:
    """Channel mapping options dto.

    Attributes:
        tuner_channels (Union[Unset, List['TunerChannelMapping']]): Gets or sets list of tuner channels.
        provider_channels (Union[Unset, List['NameIdPair']]): Gets or sets list of provider channels.
        mappings (Union[Unset, List['NameValuePair']]): Gets or sets list of mappings.
        provider_name (Union[None, Unset, str]): Gets or sets provider name.
    """

    tuner_channels: Unset | list["TunerChannelMapping"] = UNSET
    provider_channels: Unset | list["NameIdPair"] = UNSET
    mappings: Unset | list["NameValuePair"] = UNSET
    provider_name: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        tuner_channels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.tuner_channels, Unset):
            tuner_channels = []
            for tuner_channels_item_data in self.tuner_channels:
                tuner_channels_item = tuner_channels_item_data.to_dict()
                tuner_channels.append(tuner_channels_item)

        provider_channels: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.provider_channels, Unset):
            provider_channels = []
            for provider_channels_item_data in self.provider_channels:
                provider_channels_item = provider_channels_item_data.to_dict()
                provider_channels.append(provider_channels_item)

        mappings: Unset | list[dict[str, Any]] = UNSET
        if not isinstance(self.mappings, Unset):
            mappings = []
            for mappings_item_data in self.mappings:
                mappings_item = mappings_item_data.to_dict()
                mappings.append(mappings_item)

        provider_name: None | Unset | str
        if isinstance(self.provider_name, Unset):
            provider_name = UNSET
        else:
            provider_name = self.provider_name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if tuner_channels is not UNSET:
            field_dict["TunerChannels"] = tuner_channels
        if provider_channels is not UNSET:
            field_dict["ProviderChannels"] = provider_channels
        if mappings is not UNSET:
            field_dict["Mappings"] = mappings
        if provider_name is not UNSET:
            field_dict["ProviderName"] = provider_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.name_id_pair import NameIdPair
        from ..models.name_value_pair import NameValuePair
        from ..models.tuner_channel_mapping import TunerChannelMapping

        d = src_dict.copy()
        tuner_channels = []
        _tuner_channels = d.pop("TunerChannels", UNSET)
        for tuner_channels_item_data in _tuner_channels or []:
            tuner_channels_item = TunerChannelMapping.from_dict(tuner_channels_item_data)

            tuner_channels.append(tuner_channels_item)

        provider_channels = []
        _provider_channels = d.pop("ProviderChannels", UNSET)
        for provider_channels_item_data in _provider_channels or []:
            provider_channels_item = NameIdPair.from_dict(provider_channels_item_data)

            provider_channels.append(provider_channels_item)

        mappings = []
        _mappings = d.pop("Mappings", UNSET)
        for mappings_item_data in _mappings or []:
            mappings_item = NameValuePair.from_dict(mappings_item_data)

            mappings.append(mappings_item)

        def _parse_provider_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        provider_name = _parse_provider_name(d.pop("ProviderName", UNSET))

        channel_mapping_options_dto = cls(
            tuner_channels=tuner_channels,
            provider_channels=provider_channels,
            mappings=mappings,
            provider_name=provider_name,
        )

        return channel_mapping_options_dto
