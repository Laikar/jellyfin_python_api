from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthenticateUserByName")


@_attrs_define
class AuthenticateUserByName:
    """The authenticate user by name request body.

    Attributes:
        username (Union[None, Unset, str]): Gets or sets the username.
        pw (Union[None, Unset, str]): Gets or sets the plain text password.
        password (Union[None, Unset, str]): Gets or sets the sha1-hashed password.
    """

    username: None | Unset | str = UNSET
    pw: None | Unset | str = UNSET
    password: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        username: None | Unset | str
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username

        pw: None | Unset | str
        if isinstance(self.pw, Unset):
            pw = UNSET
        else:
            pw = self.pw

        password: None | Unset | str
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if username is not UNSET:
            field_dict["Username"] = username
        if pw is not UNSET:
            field_dict["Pw"] = pw
        if password is not UNSET:
            field_dict["Password"] = password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_username(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        username = _parse_username(d.pop("Username", UNSET))

        def _parse_pw(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        pw = _parse_pw(d.pop("Pw", UNSET))

        def _parse_password(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        password = _parse_password(d.pop("Password", UNSET))

        authenticate_user_by_name = cls(
            username=username,
            pw=pw,
            password=password,
        )

        return authenticate_user_by_name
