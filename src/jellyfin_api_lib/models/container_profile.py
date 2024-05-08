import builtins
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dlna_profile_type import DlnaProfileType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.profile_condition import ProfileCondition


T = TypeVar("T", bound="ContainerProfile")


@_attrs_define
class ContainerProfile:
    """
    Attributes:
        type (Union[Unset, DlnaProfileType]):
        conditions (Union[List['ProfileCondition'], None, Unset]):
        container (Union[Unset, str]):
    """

    type: Unset | DlnaProfileType = UNSET
    conditions: list["ProfileCondition"] | None | Unset = UNSET
    container: Unset | str = UNSET

    def to_dict(self) -> dict[str, Any]:
        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        conditions: list[dict[str, Any]] | None | Unset
        if isinstance(self.conditions, Unset):
            conditions = UNSET
        elif isinstance(self.conditions, list):
            conditions = []
            for conditions_type_0_item_data in self.conditions:
                conditions_type_0_item = conditions_type_0_item_data.to_dict()
                conditions.append(conditions_type_0_item)

        else:
            conditions = self.conditions

        container = self.container

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if type is not UNSET:
            field_dict["Type"] = type
        if conditions is not UNSET:
            field_dict["Conditions"] = conditions
        if container is not UNSET:
            field_dict["Container"] = container

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        from ..models.profile_condition import ProfileCondition

        d = src_dict.copy()
        _type = d.pop("Type", UNSET)
        type: Unset | DlnaProfileType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DlnaProfileType(_type)

        def _parse_conditions(data: object) -> list["ProfileCondition"] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conditions_type_0 = []
                _conditions_type_0 = data
                for conditions_type_0_item_data in _conditions_type_0:
                    conditions_type_0_item = ProfileCondition.from_dict(conditions_type_0_item_data)

                    conditions_type_0.append(conditions_type_0_item)

                return conditions_type_0
            except:  # noqa: E722
                pass
            return cast(list["ProfileCondition"] | None | Unset, data)

        conditions = _parse_conditions(d.pop("Conditions", UNSET))

        container = d.pop("Container", UNSET)

        container_profile = cls(
            type=type,
            conditions=conditions,
            container=container,
        )

        return container_profile
