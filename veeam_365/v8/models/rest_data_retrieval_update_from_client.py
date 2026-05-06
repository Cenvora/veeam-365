from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RESTDataRetrievalUpdateFromClient")



@_attrs_define
class RESTDataRetrievalUpdateFromClient:
    """ 
        Attributes:
            name (None | str | Unset): Specifies the retrieval job name.
            description (None | str | Unset): Specifies the retrieval job description.
            availability_period_days (int | None | Unset): Specifies how many days you will be able to explore and restore
                the retrieved data using Veeam Explorers.
            enable_expiration_notification (bool | None | Unset): Defines whether Veeam Backup for Microsoft 365 will send a
                notification by email before the retrieved data expires.
            expiration_hours_threshold (int | None | Unset): Specifies how many hours should remain before the retrieved
                data expires to send a notification by email.  Use this property only with the `enableExpirationNotification`
                property.
     """

    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    availability_period_days: int | None | Unset = UNSET
    enable_expiration_notification: bool | None | Unset = UNSET
    expiration_hours_threshold: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        availability_period_days: int | None | Unset
        if isinstance(self.availability_period_days, Unset):
            availability_period_days = UNSET
        else:
            availability_period_days = self.availability_period_days

        enable_expiration_notification: bool | None | Unset
        if isinstance(self.enable_expiration_notification, Unset):
            enable_expiration_notification = UNSET
        else:
            enable_expiration_notification = self.enable_expiration_notification

        expiration_hours_threshold: int | None | Unset
        if isinstance(self.expiration_hours_threshold, Unset):
            expiration_hours_threshold = UNSET
        else:
            expiration_hours_threshold = self.expiration_hours_threshold


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if availability_period_days is not UNSET:
            field_dict["availabilityPeriodDays"] = availability_period_days
        if enable_expiration_notification is not UNSET:
            field_dict["enableExpirationNotification"] = enable_expiration_notification
        if expiration_hours_threshold is not UNSET:
            field_dict["expirationHoursThreshold"] = expiration_hours_threshold

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_availability_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        availability_period_days = _parse_availability_period_days(d.pop("availabilityPeriodDays", UNSET))


        def _parse_enable_expiration_notification(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enable_expiration_notification = _parse_enable_expiration_notification(d.pop("enableExpirationNotification", UNSET))


        def _parse_expiration_hours_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expiration_hours_threshold = _parse_expiration_hours_threshold(d.pop("expirationHoursThreshold", UNSET))


        rest_data_retrieval_update_from_client = cls(
            name=name,
            description=description,
            availability_period_days=availability_period_days,
            enable_expiration_notification=enable_expiration_notification,
            expiration_hours_threshold=expiration_hours_threshold,
        )


        rest_data_retrieval_update_from_client.additional_properties = d
        return rest_data_retrieval_update_from_client

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
