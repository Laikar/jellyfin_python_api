from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.profile_condition_type import ProfileConditionType
from ..models.profile_condition_value import ProfileConditionValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProfileCondition")


@_attrs_define
class ProfileCondition:
    """
    Attributes:
        condition (Union[Unset, ProfileConditionType]):
        property_ (Union[Unset, ProfileConditionValue]):
        value (Union[None, Unset, str]):
        is_required (Union[Unset, bool]):
    """

    condition: Unset | ProfileConditionType = UNSET
    property_: Unset | ProfileConditionValue = UNSET
    value: None | Unset | str = UNSET
    is_required: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        condition: Unset | str = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.value

        property_: Unset | str = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        value: None | Unset | str
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        is_required = self.is_required

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if condition is not UNSET:
            field_dict["Condition"] = condition
        if property_ is not UNSET:
            field_dict["Property"] = property_
        if value is not UNSET:
            field_dict["Value"] = value
        if is_required is not UNSET:
            field_dict["IsRequired"] = is_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _condition = d.pop("Condition", UNSET)
        condition: Unset | ProfileConditionType
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = ProfileConditionType(_condition)

        _property_ = d.pop("Property", UNSET)
        property_: Unset | ProfileConditionValue
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = ProfileConditionValue(_property_)

        def _parse_value(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        value = _parse_value(d.pop("Value", UNSET))

        is_required = d.pop("IsRequired", UNSET)

        profile_condition = cls(
            condition=condition,
            property_=property_,
            value=value,
            is_required=is_required,
        )

        return profile_condition
