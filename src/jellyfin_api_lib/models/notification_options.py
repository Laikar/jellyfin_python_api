from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_option import NotificationOption


T = TypeVar("T", bound="NotificationOptions")


@_attrs_define
class NotificationOptions:
    """
    Attributes:
        options (Union[List['NotificationOption'], None, Unset]):
    """

    options: list["NotificationOption"] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)

        else:
            options = self.options

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if options is not UNSET:
            field_dict["Options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.notification_option import NotificationOption

        d = src_dict.copy()

        def _parse_options(data: object) -> list["NotificationOption"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in _options_type_0:
                    options_type_0_item = NotificationOption.from_dict(options_type_0_item_data)

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except:  # noqa: E722
                pass
            return cast(list["NotificationOption"] | None | Unset, data)

        options = _parse_options(d.pop("Options", UNSET))

        notification_options = cls(
            options=options,
        )

        return notification_options
