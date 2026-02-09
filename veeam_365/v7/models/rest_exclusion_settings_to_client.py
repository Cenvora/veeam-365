from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_exclusion_settings_to_client_actions import RESTExclusionSettingsToClientActions
    from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary


T = TypeVar("T", bound="RESTExclusionSettingsToClient")


@_attrs_define
class RESTExclusionSettingsToClient:
    """
    Attributes:
        field_links (RESTLinkHALDictionary | Unset):
        field_actions (RESTExclusionSettingsToClientActions | Unset):
        deleted_items (bool | None | Unset): Defines whether backup jobs will process the *Deleted Items* mailbox
            folder.
        drafts (bool | None | Unset): Defines whether backup jobs will process the *Drafts* mailbox folder.
        junk_email (bool | None | Unset): Defines whether backup jobs will process the *Junk Email* mailbox folder.
        outbox (bool | None | Unset): Defines whether backup jobs will process the *Outbox* mailbox folder.
        sync_issues (bool | None | Unset): Defines whether backup jobs will process the *Sync Issues* mailbox folder.
        litigation_hold (bool | None | Unset): Defines whether backup jobs will process the preserved items of mailboxes
            placed on Litigation Hold.
        in_place_hold (bool | None | Unset): Defines whether backup jobs will process the preserved items of mailboxes
            placed on In-Place Hold.
    """

    field_links: RESTLinkHALDictionary | Unset = UNSET
    field_actions: RESTExclusionSettingsToClientActions | Unset = UNSET
    deleted_items: bool | None | Unset = UNSET
    drafts: bool | None | Unset = UNSET
    junk_email: bool | None | Unset = UNSET
    outbox: bool | None | Unset = UNSET
    sync_issues: bool | None | Unset = UNSET
    litigation_hold: bool | None | Unset = UNSET
    in_place_hold: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        deleted_items: bool | None | Unset
        if isinstance(self.deleted_items, Unset):
            deleted_items = UNSET
        else:
            deleted_items = self.deleted_items

        drafts: bool | None | Unset
        if isinstance(self.drafts, Unset):
            drafts = UNSET
        else:
            drafts = self.drafts

        junk_email: bool | None | Unset
        if isinstance(self.junk_email, Unset):
            junk_email = UNSET
        else:
            junk_email = self.junk_email

        outbox: bool | None | Unset
        if isinstance(self.outbox, Unset):
            outbox = UNSET
        else:
            outbox = self.outbox

        sync_issues: bool | None | Unset
        if isinstance(self.sync_issues, Unset):
            sync_issues = UNSET
        else:
            sync_issues = self.sync_issues

        litigation_hold: bool | None | Unset
        if isinstance(self.litigation_hold, Unset):
            litigation_hold = UNSET
        else:
            litigation_hold = self.litigation_hold

        in_place_hold: bool | None | Unset
        if isinstance(self.in_place_hold, Unset):
            in_place_hold = UNSET
        else:
            in_place_hold = self.in_place_hold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if deleted_items is not UNSET:
            field_dict["deletedItems"] = deleted_items
        if drafts is not UNSET:
            field_dict["drafts"] = drafts
        if junk_email is not UNSET:
            field_dict["junkEmail"] = junk_email
        if outbox is not UNSET:
            field_dict["outbox"] = outbox
        if sync_issues is not UNSET:
            field_dict["syncIssues"] = sync_issues
        if litigation_hold is not UNSET:
            field_dict["litigationHold"] = litigation_hold
        if in_place_hold is not UNSET:
            field_dict["inPlaceHold"] = in_place_hold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_exclusion_settings_to_client_actions import RESTExclusionSettingsToClientActions
        from ..models.rest_link_hal_dictionary import RESTLinkHALDictionary

        d = dict(src_dict)
        _field_links = d.pop("_links", UNSET)
        field_links: RESTLinkHALDictionary | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTLinkHALDictionary.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTExclusionSettingsToClientActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTExclusionSettingsToClientActions.from_dict(_field_actions)

        def _parse_deleted_items(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        deleted_items = _parse_deleted_items(d.pop("deletedItems", UNSET))

        def _parse_drafts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        drafts = _parse_drafts(d.pop("drafts", UNSET))

        def _parse_junk_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        junk_email = _parse_junk_email(d.pop("junkEmail", UNSET))

        def _parse_outbox(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        outbox = _parse_outbox(d.pop("outbox", UNSET))

        def _parse_sync_issues(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sync_issues = _parse_sync_issues(d.pop("syncIssues", UNSET))

        def _parse_litigation_hold(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        litigation_hold = _parse_litigation_hold(d.pop("litigationHold", UNSET))

        def _parse_in_place_hold(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        in_place_hold = _parse_in_place_hold(d.pop("inPlaceHold", UNSET))

        rest_exclusion_settings_to_client = cls(
            field_links=field_links,
            field_actions=field_actions,
            deleted_items=deleted_items,
            drafts=drafts,
            junk_email=junk_email,
            outbox=outbox,
            sync_issues=sync_issues,
            litigation_hold=litigation_hold,
            in_place_hold=in_place_hold,
        )

        rest_exclusion_settings_to_client.additional_properties = d
        return rest_exclusion_settings_to_client

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
