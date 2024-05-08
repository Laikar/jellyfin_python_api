from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateUserEasyPassword")


@_attrs_define
class UpdateUserEasyPassword:
    """The update user easy password request body.

    Attributes:
        new_password (Union[None, Unset, str]): Gets or sets the new sha1-hashed password.
        new_pw (Union[None, Unset, str]): Gets or sets the new password.
        reset_password (Union[Unset, bool]): Gets or sets a value indicating whether to reset the password.
    """

    new_password: None | Unset | str = UNSET
    new_pw: None | Unset | str = UNSET
    reset_password: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        new_password: None | Unset | str
        if isinstance(self.new_password, Unset):
            new_password = UNSET
        else:
            new_password = self.new_password

        new_pw: None | Unset | str
        if isinstance(self.new_pw, Unset):
            new_pw = UNSET
        else:
            new_pw = self.new_pw

        reset_password = self.reset_password

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if new_password is not UNSET:
            field_dict["NewPassword"] = new_password
        if new_pw is not UNSET:
            field_dict["NewPw"] = new_pw
        if reset_password is not UNSET:
            field_dict["ResetPassword"] = reset_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_new_password(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        new_password = _parse_new_password(d.pop("NewPassword", UNSET))

        def _parse_new_pw(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        new_pw = _parse_new_pw(d.pop("NewPw", UNSET))

        reset_password = d.pop("ResetPassword", UNSET)

        update_user_easy_password = cls(
            new_password=new_password,
            new_pw=new_pw,
            reset_password=reset_password,
        )

        return update_user_easy_password
