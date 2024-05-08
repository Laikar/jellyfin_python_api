import datetime
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.forgot_password_action import ForgotPasswordAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="ForgotPasswordResult")


@_attrs_define
class ForgotPasswordResult:
    """
    Attributes:
        action (Union[Unset, ForgotPasswordAction]):
        pin_file (Union[None, Unset, str]): Gets or sets the pin file.
        pin_expiration_date (Union[None, Unset, datetime.datetime]): Gets or sets the pin expiration date.
    """

    action: Unset | ForgotPasswordAction = UNSET
    pin_file: None | Unset | str = UNSET
    pin_expiration_date: None | Unset | datetime.datetime = UNSET

    def to_dict(self) -> dict[str, Any]:
        action: Unset | str = UNSET
        if not isinstance(self.action, Unset):
            action = self.action.value

        pin_file: None | Unset | str
        if isinstance(self.pin_file, Unset):
            pin_file = UNSET
        else:
            pin_file = self.pin_file

        pin_expiration_date: None | Unset | str
        if isinstance(self.pin_expiration_date, Unset):
            pin_expiration_date = UNSET
        elif isinstance(self.pin_expiration_date, datetime.datetime):
            pin_expiration_date = self.pin_expiration_date.isoformat()
        else:
            pin_expiration_date = self.pin_expiration_date

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if action is not UNSET:
            field_dict["Action"] = action
        if pin_file is not UNSET:
            field_dict["PinFile"] = pin_file
        if pin_expiration_date is not UNSET:
            field_dict["PinExpirationDate"] = pin_expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _action = d.pop("Action", UNSET)
        action: Unset | ForgotPasswordAction
        if isinstance(_action, Unset):
            action = UNSET
        else:
            action = ForgotPasswordAction(_action)

        def _parse_pin_file(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pin_file = _parse_pin_file(d.pop("PinFile", UNSET))

        def _parse_pin_expiration_date(data: object) -> None | Unset | datetime.datetime:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pin_expiration_date_type_0 = isoparse(data)

                return pin_expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(None | Unset | datetime.datetime, data)

        pin_expiration_date = _parse_pin_expiration_date(d.pop("PinExpirationDate", UNSET))

        forgot_password_result = cls(
            action=action,
            pin_file=pin_file,
            pin_expiration_date=pin_expiration_date,
        )

        return forgot_password_result
