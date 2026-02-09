from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTRestorePostsOptions")


@_attrs_define
class RESTRestorePostsOptions:
    """
    Attributes:
        channel_id (str):
        from_ (datetime.datetime | None | Unset):
        to (datetime.datetime | None | Unset):
        user_code (str | Unset):
        application_id (None | Unset | UUID):  Example: 00000000-0000-0000-0000-000000000000.
        application_certificate (str | Unset):
        application_certificate_password (str | Unset):
        user_name (str | Unset):
        user_password (str | Unset):
    """

    channel_id: str
    from_: datetime.datetime | None | Unset = UNSET
    to: datetime.datetime | None | Unset = UNSET
    user_code: str | Unset = UNSET
    application_id: None | Unset | UUID = UNSET
    application_certificate: str | Unset = UNSET
    application_certificate_password: str | Unset = UNSET
    user_name: str | Unset = UNSET
    user_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.datetime):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.datetime):
            to = self.to.isoformat()
        else:
            to = self.to

        user_code = self.user_code

        application_id: None | str | Unset
        if isinstance(self.application_id, Unset):
            application_id = UNSET
        elif isinstance(self.application_id, UUID):
            application_id = str(self.application_id)
        else:
            application_id = self.application_id

        application_certificate = self.application_certificate

        application_certificate_password = self.application_certificate_password

        user_name = self.user_name

        user_password = self.user_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelId": channel_id,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if user_code is not UNSET:
            field_dict["userCode"] = user_code
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_certificate is not UNSET:
            field_dict["applicationCertificate"] = application_certificate
        if application_certificate_password is not UNSET:
            field_dict["applicationCertificatePassword"] = application_certificate_password
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if user_password is not UNSET:
            field_dict["userPassword"] = user_password

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channelId")

        def _parse_from_(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = isoparse(data)

                return from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = isoparse(data)

                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

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

        application_certificate = d.pop("applicationCertificate", UNSET)

        application_certificate_password = d.pop("applicationCertificatePassword", UNSET)

        user_name = d.pop("userName", UNSET)

        user_password = d.pop("userPassword", UNSET)

        rest_restore_posts_options = cls(
            channel_id=channel_id,
            from_=from_,
            to=to,
            user_code=user_code,
            application_id=application_id,
            application_certificate=application_certificate,
            application_certificate_password=application_certificate_password,
            user_name=user_name,
            user_password=user_password,
        )

        rest_restore_posts_options.additional_properties = d
        return rest_restore_posts_options

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
