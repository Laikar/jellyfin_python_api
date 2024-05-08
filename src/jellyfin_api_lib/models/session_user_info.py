from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionUserInfo")


@_attrs_define
class SessionUserInfo:
    """Class SessionUserInfo.

    Attributes:
        user_id (Union[Unset, str]): Gets or sets the user identifier.
        user_name (Union[None, Unset, str]): Gets or sets the name of the user.
    """

    user_id: Unset | str = UNSET
    user_name: None | Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_name: None | Unset | str
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["UserId"] = user_id
        if user_name is not UNSET:
            field_dict["UserName"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("UserId", UNSET)

        def _parse_user_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        user_name = _parse_user_name(d.pop("UserName", UNSET))

        session_user_info = cls(
            user_id=user_id,
            user_name=user_name,
        )

        return session_user_info
