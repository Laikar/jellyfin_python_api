from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataConfiguration")


@_attrs_define
class MetadataConfiguration:
    """
    Attributes:
        use_file_creation_time_for_date_added (Union[Unset, bool]):
    """

    use_file_creation_time_for_date_added: Unset | bool = UNSET

    def to_dict(self) -> dict[str, Any]:
        use_file_creation_time_for_date_added = self.use_file_creation_time_for_date_added

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if use_file_creation_time_for_date_added is not UNSET:
            field_dict["UseFileCreationTimeForDateAdded"] = use_file_creation_time_for_date_added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        use_file_creation_time_for_date_added = d.pop("UseFileCreationTimeForDateAdded", UNSET)

        metadata_configuration = cls(
            use_file_creation_time_for_date_added=use_file_creation_time_for_date_added,
        )

        return metadata_configuration
