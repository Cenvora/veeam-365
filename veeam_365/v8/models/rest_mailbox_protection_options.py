from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_mailbox_protection_options_format import RESTMailboxProtectionOptionsFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTMailboxProtectionOptions")


@_attrs_define
class RESTMailboxProtectionOptions:
    """
    Attributes:
        organization_id (None | Unset | UUID): Specifies the ID of an organization for which the mailbox protection
            report will be generated. Example: 00000000-0000-0000-0000-000000000000.
        format_ (RESTMailboxProtectionOptionsFormat | Unset): Specifies the format in which to save a report.
        timezone (str | Unset): Specifies a time zone for the reporting interval. If you do not specify this property,
            the server will generate a report for the UTC time zone.
    """

    organization_id: None | Unset | UUID = UNSET
    format_: RESTMailboxProtectionOptionsFormat | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if format_ is not UNSET:
            field_dict["format"] = format_
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        _format_ = d.pop("format", UNSET)
        format_: RESTMailboxProtectionOptionsFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = RESTMailboxProtectionOptionsFormat(_format_)

        timezone = d.pop("timezone", UNSET)

        rest_mailbox_protection_options = cls(
            organization_id=organization_id,
            format_=format_,
            timezone=timezone,
        )

        rest_mailbox_protection_options.additional_properties = d
        return rest_mailbox_protection_options

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
