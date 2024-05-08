from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageByNameInfo")


@_attrs_define
class ImageByNameInfo:
    """
    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        theme (Union[None, Unset, str]): Gets or sets the theme.
        context (Union[None, Unset, str]): Gets or sets the context.
        file_length (Union[Unset, int]): Gets or sets the length of the file.
        format_ (Union[None, Unset, str]): Gets or sets the format.
    """

    name: None | Unset | str = UNSET
    theme: None | Unset | str = UNSET
    context: None | Unset | str = UNSET
    file_length: Unset | int = UNSET
    format_: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        theme: None | Unset | str
        if isinstance(self.theme, Unset):
            theme = UNSET
        else:
            theme = self.theme

        context: None | Unset | str
        if isinstance(self.context, Unset):
            context = UNSET
        else:
            context = self.context

        file_length = self.file_length

        format_: None | Unset | str
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if theme is not UNSET:
            field_dict["Theme"] = theme
        if context is not UNSET:
            field_dict["Context"] = context
        if file_length is not UNSET:
            field_dict["FileLength"] = file_length
        if format_ is not UNSET:
            field_dict["Format"] = format_

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

        def _parse_theme(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        theme = _parse_theme(d.pop("Theme", UNSET))

        def _parse_context(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        context = _parse_context(d.pop("Context", UNSET))

        file_length = d.pop("FileLength", UNSET)

        def _parse_format_(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        format_ = _parse_format_(d.pop("Format", UNSET))

        image_by_name_info = cls(
            name=name,
            theme=theme,
            context=context,
            file_length=file_length,
            format_=format_,
        )

        return image_by_name_info
