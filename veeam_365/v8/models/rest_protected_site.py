from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTProtectedSite")


@_attrs_define
class RESTProtectedSite:
    """
    Attributes:
        id (str | Unset): SharePoint site ID.
        msid (str | Unset): ID of the protected site assigned by Microsoft.
        display_name (str | Unset): Display name of the SharePoint site.
        url (str | Unset): SharePoint site path.
        organization_id (None | Unset | UUID): Backed-up organization ID. Example: 00000000-0000-0000-0000-000000000000.
        backed_up_organization_id (str | Unset): ID of the backed-up organization in the backup.
        e_tag (int | Unset): Version number that Veeam Backup for Microsoft 365 assigns if the protected site was
            modified.
    """

    id: str | Unset = UNSET
    msid: str | Unset = UNSET
    display_name: str | Unset = UNSET
    url: str | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    e_tag: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        msid = self.msid

        display_name = self.display_name

        url = self.url

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id = self.backed_up_organization_id

        e_tag = self.e_tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if msid is not UNSET:
            field_dict["msid"] = msid
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if url is not UNSET:
            field_dict["url"] = url
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if e_tag is not UNSET:
            field_dict["eTag"] = e_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        msid = d.pop("msid", UNSET)

        display_name = d.pop("displayName", UNSET)

        url = d.pop("url", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)

                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organizationId", UNSET))

        backed_up_organization_id = d.pop("backedUpOrganizationId", UNSET)

        e_tag = d.pop("eTag", UNSET)

        rest_protected_site = cls(
            id=id,
            msid=msid,
            display_name=display_name,
            url=url,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            e_tag=e_tag,
        )

        rest_protected_site.additional_properties = d
        return rest_protected_site

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
