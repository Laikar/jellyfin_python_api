from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartupConfigurationDto")


@_attrs_define
class StartupConfigurationDto:
    """The startup configuration DTO.

    Attributes:
        ui_culture (Union[None, Unset, str]): Gets or sets UI language culture.
        metadata_country_code (Union[None, Unset, str]): Gets or sets the metadata country code.
        preferred_metadata_language (Union[None, Unset, str]): Gets or sets the preferred language for the metadata.
    """

    ui_culture: None | Unset | str = UNSET
    metadata_country_code: None | Unset | str = UNSET
    preferred_metadata_language: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        ui_culture: None | Unset | str
        if isinstance(self.ui_culture, Unset):
            ui_culture = UNSET
        else:
            ui_culture = self.ui_culture

        metadata_country_code: None | Unset | str
        if isinstance(self.metadata_country_code, Unset):
            metadata_country_code = UNSET
        else:
            metadata_country_code = self.metadata_country_code

        preferred_metadata_language: None | Unset | str
        if isinstance(self.preferred_metadata_language, Unset):
            preferred_metadata_language = UNSET
        else:
            preferred_metadata_language = self.preferred_metadata_language

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if ui_culture is not UNSET:
            field_dict["UICulture"] = ui_culture
        if metadata_country_code is not UNSET:
            field_dict["MetadataCountryCode"] = metadata_country_code
        if preferred_metadata_language is not UNSET:
            field_dict["PreferredMetadataLanguage"] = preferred_metadata_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_ui_culture(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        ui_culture = _parse_ui_culture(d.pop("UICulture", UNSET))

        def _parse_metadata_country_code(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        metadata_country_code = _parse_metadata_country_code(d.pop("MetadataCountryCode", UNSET))

        def _parse_preferred_metadata_language(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        preferred_metadata_language = _parse_preferred_metadata_language(d.pop("PreferredMetadataLanguage", UNSET))

        startup_configuration_dto = cls(
            ui_culture=ui_culture,
            metadata_country_code=metadata_country_code,
            preferred_metadata_language=preferred_metadata_language,
        )

        return startup_configuration_dto
