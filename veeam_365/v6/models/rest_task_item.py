from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rest_task_item_status import RESTTaskItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_task_item_actions import RESTTaskItemActions
    from ..models.rest_task_item_links import RESTTaskItemLinks


T = TypeVar("T", bound="RESTTaskItem")


@_attrs_define
class RESTTaskItem:
    """
    Attributes:
        status (RESTTaskItemStatus | Unset):
        percent_complete (float | Unset):
        start_date (datetime.datetime | Unset):
        due_date (datetime.datetime | Unset):
        owner (str | Unset):
        subject (str | Unset):
        item_class (str | Unset):
        field_links (RESTTaskItemLinks | Unset):
        field_actions (RESTTaskItemActions | Unset):
        id (str | Unset):
    """

    status: RESTTaskItemStatus | Unset = UNSET
    percent_complete: float | Unset = UNSET
    start_date: datetime.datetime | Unset = UNSET
    due_date: datetime.datetime | Unset = UNSET
    owner: str | Unset = UNSET
    subject: str | Unset = UNSET
    item_class: str | Unset = UNSET
    field_links: RESTTaskItemLinks | Unset = UNSET
    field_actions: RESTTaskItemActions | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        percent_complete = self.percent_complete

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        due_date: str | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        owner = self.owner

        subject = self.subject

        item_class = self.item_class

        field_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_actions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_actions, Unset):
            field_actions = self.field_actions.to_dict()

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if percent_complete is not UNSET:
            field_dict["percentComplete"] = percent_complete
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if owner is not UNSET:
            field_dict["owner"] = owner
        if subject is not UNSET:
            field_dict["subject"] = subject
        if item_class is not UNSET:
            field_dict["itemClass"] = item_class
        if field_links is not UNSET:
            field_dict["_links"] = field_links
        if field_actions is not UNSET:
            field_dict["_actions"] = field_actions
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_task_item_actions import RESTTaskItemActions
        from ..models.rest_task_item_links import RESTTaskItemLinks

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: RESTTaskItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RESTTaskItemStatus(_status)

        percent_complete = d.pop("percentComplete", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.datetime | Unset
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _due_date = d.pop("dueDate", UNSET)
        due_date: datetime.datetime | Unset
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        owner = d.pop("owner", UNSET)

        subject = d.pop("subject", UNSET)

        item_class = d.pop("itemClass", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: RESTTaskItemLinks | Unset
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = RESTTaskItemLinks.from_dict(_field_links)

        _field_actions = d.pop("_actions", UNSET)
        field_actions: RESTTaskItemActions | Unset
        if isinstance(_field_actions, Unset):
            field_actions = UNSET
        else:
            field_actions = RESTTaskItemActions.from_dict(_field_actions)

        id = d.pop("id", UNSET)

        rest_task_item = cls(
            status=status,
            percent_complete=percent_complete,
            start_date=start_date,
            due_date=due_date,
            owner=owner,
            subject=subject,
            item_class=item_class,
            field_links=field_links,
            field_actions=field_actions,
            id=id,
        )

        rest_task_item.additional_properties = d
        return rest_task_item

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
