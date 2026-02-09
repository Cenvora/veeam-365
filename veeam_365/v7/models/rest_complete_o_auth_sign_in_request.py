from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_complete_o_auth_sign_in_request_actions import RESTCompleteOAuthSignInRequestActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTCompleteOAuthSignInRequest")


@_attrs_define
class RESTCompleteOAuthSignInRequest:
    """
    Attributes:
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTCompleteOAuthSignInRequestActions | Unset):
        code (str | Unset): Specifies value that you get from the Google Authorization Server or Microsoft
            authentication portal in the redirect URL. Veeam Backup for Microsoft 365 will use this value to obtain an
            access token.
        state (str | Unset): Specifies value that you get from the Google Authorization Server or Microsoft
            authentication portal in the redirect URL. Veeam Backup for Microsoft 365 will use this value to check that the
            `code` property value matches the authentication request.
        error (str | Unset): Specifies an error if occurred during the preparation step.
        error_description (str | Unset): Specifies an error description.
    """

    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTCompleteOAuthSignInRequestActions | Unset = UNSET
    code: str | Unset = UNSET
    state: str | Unset = UNSET
    error: str | Unset = UNSET
    error_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        code = self.code

        state = self.state

        error = self.error

        error_description = self.error_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if code is not UNSET:
            field_dict["code"] = code
        if state is not UNSET:
            field_dict["state"] = state
        if error is not UNSET:
            field_dict["error"] = error
        if error_description is not UNSET:
            field_dict["errorDescription"] = error_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_complete_o_auth_sign_in_request_actions import RESTCompleteOAuthSignInRequestActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTCompleteOAuthSignInRequestActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTCompleteOAuthSignInRequestActions.from_dict(_field_actions)

        code = d.pop("code", UNSET)

        state = d.pop("state", UNSET)

        error = d.pop("error", UNSET)

        error_description = d.pop("errorDescription", UNSET)

        rest_complete_o_auth_sign_in_request = cls(
            field_links=field_links,
            field_actions=field_actions,
            code=code,
            state=state,
            error=error,
            error_description=error_description,
        )

        rest_complete_o_auth_sign_in_request.additional_properties = d
        return rest_complete_o_auth_sign_in_request

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
