from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTOrganizationLicensingInformation")


@_attrs_define
class RESTOrganizationLicensingInformation:
    """
    Attributes:
        licensed_users (int | Unset): Number of Veeam licenses that users consume at the moment.

            Veeam Backup for Microsoft 365 can temporarily provide you with extra licenses if the number of used licenses
            exceeds the limit. For more information about licensing in Veeam Backup for Microsoft 365, see the [Licensing
            and License Types](https://helpcenter.veeam.com/docs/vbo365/guide/vbo_licensing.html?ver=80) section of the
            Veeam Backup for Microsoft 365 User Guide.

            This property value shows the total number of the licensed users and users that exceed the license limit.
        new_users (int | Unset): Number of the Veeam licenses that remain unconsumed at the moment.

            If you have *Subscription License*, this property value is *0*. If you have *Rental License*, this property
            value shows the number of users with the *new user* status. For more information about user accounts with the
            *new user* status, see the [Rental
            License](https://helpcenter.veeam.com/docs/vbo365/guide/vbo_rental_license.html?ver=80#new-user) section of the
            Veeam Backup for Microsoft 365 User Guide.
    """

    licensed_users: int | Unset = UNSET
    new_users: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        licensed_users = self.licensed_users

        new_users = self.new_users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if licensed_users is not UNSET:
            field_dict["licensedUsers"] = licensed_users
        if new_users is not UNSET:
            field_dict["newUsers"] = new_users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        licensed_users = d.pop("licensedUsers", UNSET)

        new_users = d.pop("newUsers", UNSET)

        rest_organization_licensing_information = cls(
            licensed_users=licensed_users,
            new_users=new_users,
        )

        rest_organization_licensing_information.additional_properties = d
        return rest_organization_licensing_information

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
