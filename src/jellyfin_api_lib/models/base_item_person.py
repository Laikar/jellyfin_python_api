import builtins
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_item_person_image_blur_hashes_type_0 import BaseItemPersonImageBlurHashesType0


T = TypeVar("T", bound="BaseItemPerson")


@_attrs_define
class BaseItemPerson:
    """This is used by the api to get information about a Person within a BaseItem.

    Attributes:
        name (Union[None, Unset, str]): Gets or sets the name.
        id (Union[Unset, str]): Gets or sets the identifier.
        role (Union[None, Unset, str]): Gets or sets the role.
        type (Union[None, Unset, str]): Gets or sets the type.
        primary_image_tag (Union[None, Unset, str]): Gets or sets the primary image tag.
        image_blur_hashes (Union['BaseItemPersonImageBlurHashesType0', None, Unset]): Gets or sets the primary image
            blurhash.
    """

    name: None | Unset | str = UNSET
    id: Unset | str = UNSET
    role: None | Unset | str = UNSET
    type: None | Unset | str = UNSET
    primary_image_tag: None | Unset | str = UNSET
    image_blur_hashes: Union["BaseItemPersonImageBlurHashesType0", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_item_person_image_blur_hashes_type_0 import BaseItemPersonImageBlurHashesType0

        name: None | Unset | str
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        id = self.id

        role: None | Unset | str
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        type: None | Unset | str
        if isinstance(self.type, Unset):
            type = UNSET
        else:
            type = self.type

        primary_image_tag: None | Unset | str
        if isinstance(self.primary_image_tag, Unset):
            primary_image_tag = UNSET
        else:
            primary_image_tag = self.primary_image_tag

        image_blur_hashes: dict[str, Any] | None | Unset
        if isinstance(self.image_blur_hashes, Unset):
            image_blur_hashes = UNSET
        elif isinstance(self.image_blur_hashes, BaseItemPersonImageBlurHashesType0):
            image_blur_hashes = self.image_blur_hashes.to_dict()
        else:
            image_blur_hashes = self.image_blur_hashes

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if name is not UNSET:
            field_dict["Name"] = name
        if id is not UNSET:
            field_dict["Id"] = id
        if role is not UNSET:
            field_dict["Role"] = role
        if type is not UNSET:
            field_dict["Type"] = type
        if primary_image_tag is not UNSET:
            field_dict["PrimaryImageTag"] = primary_image_tag
        if image_blur_hashes is not UNSET:
            field_dict["ImageBlurHashes"] = image_blur_hashes

        return field_dict

    @classmethod
    def from_dict(cls: builtins.type[T], src_dict: dict[str, Any]) -> T:
        from ..models.base_item_person_image_blur_hashes_type_0 import BaseItemPersonImageBlurHashesType0

        d = src_dict.copy()

        def _parse_name(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        name = _parse_name(d.pop("Name", UNSET))

        id = d.pop("Id", UNSET)

        def _parse_role(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        role = _parse_role(d.pop("Role", UNSET))

        def _parse_type(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        type = _parse_type(d.pop("Type", UNSET))

        def _parse_primary_image_tag(data: object) -> None | Unset | str:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | Unset | str, data)

        primary_image_tag = _parse_primary_image_tag(d.pop("PrimaryImageTag", UNSET))

        def _parse_image_blur_hashes(data: object) -> Union["BaseItemPersonImageBlurHashesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_blur_hashes_type_0 = BaseItemPersonImageBlurHashesType0.from_dict(data)

                return image_blur_hashes_type_0
            except:  # noqa: E722
                pass
            return cast(Union["BaseItemPersonImageBlurHashesType0", None, Unset], data)

        image_blur_hashes = _parse_image_blur_hashes(d.pop("ImageBlurHashes", UNSET))

        base_item_person = cls(
            name=name,
            id=id,
            role=role,
            type=type,
            primary_image_tag=primary_image_tag,
            image_blur_hashes=image_blur_hashes,
        )

        return base_item_person
