from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_complete_o_auth_sign_in_response_actions import RESTCompleteOAuthSignInResponseActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTCompleteOAuthSignInResponse")


@_attrs_define
class RESTCompleteOAuthSignInResponse:
    """
    Attributes:
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTCompleteOAuthSignInResponseActions | Unset):
        request_id (str | Unset): Auhentication request ID.
        user_id (str | Unset): Authenticated user account ID. Veeam Backup for Microsoft 365 will send email
            notifications on behalf of this user.
    """

    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTCompleteOAuthSignInResponseActions | Unset = UNSET
    request_id: str | Unset = UNSET
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        request_id = self.request_id

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_complete_o_auth_sign_in_response_actions import RESTCompleteOAuthSignInResponseActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTCompleteOAuthSignInResponseActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTCompleteOAuthSignInResponseActions.from_dict(_field_actions)

        request_id = d.pop("requestId", UNSET)

        user_id = d.pop("userId", UNSET)

        rest_complete_o_auth_sign_in_response = cls(
            field_links=field_links,
            field_actions=field_actions,
            request_id=request_id,
            user_id=user_id,
        )

        rest_complete_o_auth_sign_in_response.additional_properties = d
        return rest_complete_o_auth_sign_in_response

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
