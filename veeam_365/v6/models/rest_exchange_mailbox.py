from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exchange_mailbox_actions import RESTExchangeMailboxActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTExchangeMailbox")


@_attrs_define
class RESTExchangeMailbox:
    """
    Attributes:
        id (UUID | Unset):  Example: 00000000-0000-0000-0000-000000000000.
        name (str | Unset):
        email (str | Unset):
        is_archive (bool | Unset):
        is_public (bool | Unset):
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTExchangeMailboxActions | Unset):
    """

    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    is_archive: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTExchangeMailboxActions | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        email = self.email

        is_archive = self.is_archive

        is_public = self.is_public

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if is_archive is not UNSET:
            field_dict["isArchive"] = is_archive
        if is_public is not UNSET:
            field_dict["isPublic"] = is_public
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_mailbox_actions import RESTExchangeMailboxActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        is_archive = d.pop("isArchive", UNSET)

        is_public = d.pop("isPublic", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTExchangeMailboxActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTExchangeMailboxActions.from_dict(_field_actions)

        rest_exchange_mailbox = cls(
            id=id,
            name=name,
            email=email,
            is_archive=is_archive,
            is_public=is_public,
            field_links=field_links,
            field_actions=field_actions,
        )

        rest_exchange_mailbox.additional_properties = d
        return rest_exchange_mailbox

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
