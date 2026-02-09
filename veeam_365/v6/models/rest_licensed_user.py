from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_licensed_user_license_state import RESTLicensedUserLicenseState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTLicensedUser")


@_attrs_define
class RESTLicensedUser:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        is_backed_up (bool | Unset):
        last_backup_date (datetime.datetime | Unset):
        license_state (RESTLicensedUserLicenseState | Unset):
        organization_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        backed_up_organization_id (str | Unset):
        organization_name (str | Unset):
        field_links (RESTLinkHALDictionary | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    is_backed_up: bool | Unset = UNSET
    last_backup_date: datetime.datetime | Unset = UNSET
    license_state: RESTLicensedUserLicenseState | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    backed_up_organization_id: str | Unset = UNSET
    organization_name: str | Unset = UNSET
    field_links: RESTLinkHALDictionary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        is_backed_up = self.is_backed_up

        last_backup_date: str | Unset = UNSET
        if not isinstance(self.last_backup_date, Unset):
            last_backup_date = self.last_backup_date.isoformat()

        license_state: str | Unset = UNSET
        if not isinstance(self.license_state, Unset):
            license_state = self.license_state.value

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        backed_up_organization_id = self.backed_up_organization_id

        organization_name = self.organization_name

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if is_backed_up is not UNSET:
            field_dict["isBackedUp"] = is_backed_up
        if last_backup_date is not UNSET:
            field_dict["lastBackupDate"] = last_backup_date
        if license_state is not UNSET:
            field_dict["licenseState"] = license_state
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if backed_up_organization_id is not UNSET:
            field_dict["backedUpOrganizationId"] = backed_up_organization_id
        if organization_name is not UNSET:
            field_dict["organizationName"] = organization_name
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        is_backed_up = d.pop("isBackedUp", UNSET)

        _last_backup_date = d.pop("lastBackupDate", UNSET)
        last_backup_date: datetime.datetime | Unset
        if isinstance(_last_backup_date, Unset):
            last_backup_date = UNSET
        else:
            last_backup_date = isoparse(_last_backup_date)

        _license_state = d.pop("licenseState", UNSET)
        license_state: RESTLicensedUserLicenseState | Unset
        if isinstance(_license_state, Unset):
            license_state = UNSET
        else:
            license_state = RESTLicensedUserLicenseState(_license_state)

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

        organization_name = d.pop("organizationName", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        rest_licensed_user = cls(
            id=id,
            name=name,
            is_backed_up=is_backed_up,
            last_backup_date=last_backup_date,
            license_state=license_state,
            organization_id=organization_id,
            backed_up_organization_id=backed_up_organization_id,
            organization_name=organization_name,
            field_links=field_links,
        )

        rest_licensed_user.additional_properties = d
        return rest_licensed_user

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
