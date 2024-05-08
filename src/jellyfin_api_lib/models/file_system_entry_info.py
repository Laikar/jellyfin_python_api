import builtins
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.file_system_entry_type import FileSystemEntryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSystemEntryInfo")


@_attrs_define
class FileSystemEntryInfo:
    """Class FileSystemEntryInfo.

    Attributes:
        name (Union[Unset, str]): Gets the name.
        path (Union[Unset, str]): Gets the path.
        type (Union[Unset, FileSystemEntryType]): Enum FileSystemEntryType.
    """

    name: Unset | str = UNSET
    path: Unset | str = UNSET
    type: Unset | FileSystemEntryType = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        type: Unset | str = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if path is not UNSET:
            field_dict["Path"] = path
        if type is not UNSET:
            field_dict["Type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("Name", UNSET)

        path = d.pop("Path", UNSET)

        _type = d.pop("Type", UNSET)
        type: Unset | FileSystemEntryType
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = FileSystemEntryType(_type)

        file_system_entry_info = cls(
            name=name,
            path=path,
            type=type,
        )

        return file_system_entry_info
