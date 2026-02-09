from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId


T = TypeVar("T", bound="RESTRestoreToOriginalLocationSelectedItems")


@_attrs_define
class RESTRestoreToOriginalLocationSelectedItems:
    """
    Attributes:
        user_name (str | Unset): Specifies the user name that you want to use for authenticating to the Exchange
            organization.
        user_password (str | Unset): Specifies a password.
        user_code (str | Unset): Specifies the authentication code. For more information on how to get a device code,
            see [Get Device Code](RestoreSession#operation/RestoreSession_DeviceCodeAction).
            This property is required if you want to use a device code for data restore.
        application_id (None | Unset | UUID): Specifies the ID of the Microsoft Entra application that you want to use
            for restore. Example: 00000000-0000-0000-0000-000000000000.
        application_certificate_password (str | Unset): Specifies a password.
        application_certificate (str | Unset): Specifies the SSL certificate configured for the Microsoft Entra
            application that you want to use for data restore. You must provide the certificate as a Base64 string.
        impersonation_account_name (str | Unset): Specifies a user name of the account that will be used as a Microsoft
            Exchange account to restore backed-up mailbox items.

            **Note**: This property is required if you want to use an application certificate for data restore. Use this
            property only with the `applicationCertificate` property.
        items (list[RESTExchangeItemStringId] | Unset): Specifies IDs of the mailbox items that you want to restore. For
            more information on how to get such IDs, see [Get Mailbox Items](ExchangeItem#operation/ExchangeItem_Get).
    """

    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate_password: str | Unset = UNSET
    application_certificate: str | Unset = UNSET
    impersonation_account_name: str | Unset = UNSET
    items: list[RESTExchangeItemStringId] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_name = self.user_name

        user_password = self.user_password

        user_code = self.user_code

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate_password = self.application_certificate_password

        application_certificate = self.application_certificate

        impersonation_account_name = self.impersonation_account_name

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if impersonation_account_name is not UNSET:
            field_dict["impersonationAccountName"] = impersonation_account_name
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exchange_item_string_id import RESTExchangeItemStringId

        d = dict(src_dict)
        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        user_code = d.pop("userCode", UNSET)

        def _parse_application_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_id_type_0 = UUID(data)

                return application_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_id = _parse_application_id(d.pop("applicationId", UNSET))

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        application_certificate = d.pop("applicationCertificate", UNSET)

        impersonation_account_name = d.pop("impersonationAccountName", UNSET)

        _items = d.pop("items", UNSET)
        items: list[RESTExchangeItemStringId] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = RESTExchangeItemStringId.from_dict(items_item_data)

                items.append(items_item)

        rest_restore_to_original_location_selected_items = cls(
            user_name=user_name,
            user_password=user_password,
            user_code=user_code,
            application_id=application_id,
            application_certificate_password=application_certificate_password,
            application_certificate=application_certificate,
            impersonation_account_name=impersonation_account_name,
            items=items,
        )

        rest_restore_to_original_location_selected_items.additional_properties = d
        return rest_restore_to_original_location_selected_items

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
