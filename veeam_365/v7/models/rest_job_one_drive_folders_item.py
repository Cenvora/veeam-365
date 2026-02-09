from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_backup_item_type import RESTJobBackupItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_job_one_drive_folders_item_links_type_0 import RESTJobOneDriveFoldersItemLinksType0


T = TypeVar("T", bound="RESTJobOneDriveFoldersItem")


@_attrs_define
class RESTJobOneDriveFoldersItem:
    """
    Attributes:
        type_ (RESTJobBackupItemType | Unset): Type of the backup item.
        folders (list[str] | Unset): Array of OneDrive folders included in/excluded from the backup job.

            **Note**: This property applies to all OneDrives in an organization. Only specified folders will be processed
            for each OneDrive.
        id (None | str | Unset): ID of a backup item.

            **Note**: This complex ID comprises the combination of the unchangeable identificator of an object type in Veeam
            Backup for Microsoft 365 and ID of a particular object. Unchangeable identificators have different values
            depending on an object type. You can use the following values to recognize objects of a particular type in the
            response: <ul>  <li>*2b38d840-8098-4614-b369-ebce33f9b2c7* - for organization users.</li>
            <li>*9592732d-22d8-426a-8167-d9635158e945* - for organization groups.</li>
            <li>*e1fa728c-4150-4724-ab3b-5deda33db0cf* - for organization sites.</li>
            <li>*c37da450-6c4b-48c4-87e2-cc557ef5d897* - for organizations.</li>  <li>*9a01bcb3-d2de-4271-96bb-95611ddc70b3*
            - for personal sites.</li>  <li>*7f07820e-9e77-4beb-92a3-b31f30bc192c* - for OneDrive folders.</li>
            <li>*7B985334-BC0E-4791-B30C-D03A1FECC840* - for teams.</li>  </ul>
        field_links (None | RESTJobOneDriveFoldersItemLinksType0 | Unset):
    """

    type_: RESTJobBackupItemType | Unset = UNSET
    folders: list[str] | Unset = UNSET
    id: None | str | Unset = UNSET
    field_links: None | RESTJobOneDriveFoldersItemLinksType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_job_one_drive_folders_item_links_type_0 import RESTJobOneDriveFoldersItemLinksType0

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        folders: list[str] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_links: dict[str, Any] | None | Unset
        if isinstance(self.field_links, Unset):
            field_links = UNSET
        elif isinstance(self.field_links, RESTJobOneDriveFoldersItemLinksType0):
            field_links = self.field_links.to_dict()
        else:
            field_links = self.field_links

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if folders is not UNSET:
            field_dict["folders"] = folders
        if id is not UNSET:
            field_dict["id"] = id
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_job_one_drive_folders_item_links_type_0 import RESTJobOneDriveFoldersItemLinksType0

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: RESTJobBackupItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = RESTJobBackupItemType(_type_)

        folders = cast(list[str], d.pop("folders", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_field_links(data: object) -> None | RESTJobOneDriveFoldersItemLinksType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_links_type_0 = RESTJobOneDriveFoldersItemLinksType0.from_dict(data)

                return field_links_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RESTJobOneDriveFoldersItemLinksType0 | Unset, data)

        field_links = _parse_field_links(d.pop("_links", UNSET))

        rest_job_one_drive_folders_item = cls(
            type_=type_,
            folders=folders,
            id=id,
            field_links=field_links,
        )

        rest_job_one_drive_folders_item.additional_properties = d
        return rest_job_one_drive_folders_item

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
