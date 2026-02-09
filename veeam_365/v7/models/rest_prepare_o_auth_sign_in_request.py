from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resto_auth_2_service_kind import RESTOAuth2ServiceKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
    from ..models.rest_prepare_o_auth_sign_in_request_actions import RESTPrepareOAuthSignInRequestActions


T = TypeVar("T", bound="RESTPrepareOAuthSignInRequest")


@_attrs_define
class RESTPrepareOAuthSignInRequest:
    """
    Attributes:
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTPrepareOAuthSignInRequestActions | Unset):
        authentication_service_kind (RESTOAuth2ServiceKind | Unset): Specifies account that you want to use to acquire
            an access token from Google or Microsoft Azure.
        client_id (None | str | Unset): Specifies a client ID obtained while registering an application in the Google
            Cloud console or Microsoft Azure portal.
        client_secret (str | Unset): Specifies a password.
        tenant_id (None | str | Unset): Specifies a tenant ID in Azure Active Directory.
        redirect_url (str | Unset): Specifies URL to which you will be redirected after signing in to Google or
            Microsoft authentication portal to get the `code` and `state` properties required to complete authentication.
            For more information, see **Complete Authentication**.
    """

    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTPrepareOAuthSignInRequestActions | Unset = UNSET
    authentication_service_kind: RESTOAuth2ServiceKind | Unset = UNSET
    client_id: None | str | Unset = UNSET
    client_secret: str | Unset = UNSET
    tenant_id: None | str | Unset = UNSET
    redirect_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

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
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
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
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary
        from ..models.rest_prepare_o_auth_sign_in_request_actions import RESTPrepareOAuthSignInRequestActions

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTPrepareOAuthSignInRequestActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTPrepareOAuthSignInRequestActions.from_dict(_field_actions)

        _authentication_service_kind = d.pop("authenticationServiceKind", UNSET)
        authentication_service_kind: RESTOAuth2ServiceKind | Unset
        if isinstance(_authentication_service_kind, Unset):
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
            field_links=field_links,
            field_actions=field_actions,
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
