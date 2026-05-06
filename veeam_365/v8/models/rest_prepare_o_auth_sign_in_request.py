from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.resto_auth_2_service_kind import RESTOAuth2ServiceKind
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RESTPrepareOAuthSignInRequest")



@_attrs_define
class RESTPrepareOAuthSignInRequest:
    """ 
        Attributes:
            authentication_service_kind (RESTOAuth2ServiceKind | Unset): Specifies account that you want to use to acquire
                an access token from Google or Microsoft Identity platform.
            client_id (None | str | Unset): Specifies a client ID obtained while registering an application in the Google
                Cloud console or Microsoft Identity platform.
            client_secret (str | Unset): Specifies a password.
            tenant_id (None | str | Unset): Specifies a tenant ID in Microsoft Entra ID.
            redirect_url (str | Unset): Specifies URL to which you will be redirected after signing in to Google or
                Microsoft Identity platform to get the `code` and `state` properties required to complete authentication. For
                more information, see **Complete Authentication**.
     """

    authentication_service_kind: RESTOAuth2ServiceKind | Unset = UNSET
    client_id: None | str | Unset = UNSET
    client_secret: str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        authentication_service_kind: str | Unset = UNSET
        if not isinstance(self.authentication_service_kind, Unset):
            authentication_service_kind = self.authentication_service_kind.value


        client_id: None | str | Unset
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        client_secret = self.client_secret

        tenant_id: None | str | Unset
        if isinstance(self.tenant_id, Unset):
            tenant_id = UNSET
        else:
            tenant_id = self.tenant_id

        redirect_url = self.redirect_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if authentication_service_kind is not UNSET:
            field_dict["authenticationServiceKind"] = authentication_service_kind
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret
        if tenant_id is not UNSET:
            field_dict["tenantId"] = tenant_id
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _authentication_service_kind = d.pop("authenticationServiceKind", UNSET)
        authentication_service_kind: RESTOAuth2ServiceKind | Unset
        if isinstance(_authentication_service_kind,  Unset):
            authentication_service_kind = UNSET
        else:
            authentication_service_kind = RESTOAuth2ServiceKind(_authentication_service_kind)




        def _parse_client_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_id = _parse_client_id(d.pop("clientId", UNSET))


        client_secret = d.pop("clientSecret", UNSET)

        def _parse_tenant_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tenant_id = _parse_tenant_id(d.pop("tenantId", UNSET))


        redirect_url = d.pop("redirectUrl", UNSET)

        rest_prepare_o_auth_sign_in_request = cls(
            authentication_service_kind=authentication_service_kind,
            client_id=client_id,
            client_secret=client_secret,
            tenant_id=tenant_id,
            redirect_url=redirect_url,
        )


        rest_prepare_o_auth_sign_in_request.additional_properties = d
        return rest_prepare_o_auth_sign_in_request

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
