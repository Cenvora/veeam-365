from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_teams_file import RESTTeamsFile


T = TypeVar("T", bound="RESTFilesSendOptions")


@_attrs_define
class RESTFilesSendOptions:
    """
    Attributes:
        channel_id (str | Unset): Specifies the ID of the channel whose files you want to send. Veeam Explorer for
            Microsoft Teams will send all files of this channel. For more information on how to get this parameter, see [Get
            Team Channels](#tag/TeamsChannel/operation/TeamsChannel_Get).

            **Note**: You do not need to use this property if you use the `files` property to specify what files to send.
        files (list[RESTTeamsFile] | Unset): Specifies IDs of files that you want to send. The files must reside in the
            same channel. For more information on how to get such IDs, see [Get
            Files](#tag/TeamsFile/operation/TeamsFile_GetPage).

            **Note**: You do not need to use this property if you use the `channelId` property to specify a channel whose
            files to send.
        from_ (str | Unset): Specifies the email address from which the attachments will be sent.
        to (str | Unset): Specifies the email address to which the attachments will be sent.
        subject (str | Unset): Specifies the subject of the email message used for sending the attachments.
        text (str | Unset): Specifies the body of the email message used for sending the attachments.
    """

    channel_id: str | Unset = UNSET
    files: list[RESTTeamsFile] | Unset = UNSET
    from_: str | Unset = UNSET
    to: str | Unset = UNSET
    subject: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        from_ = self.from_

        to = self.to

        subject = self.subject

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_id is not UNSET:
            field_dict["channelId"] = channel_id
        if files is not UNSET:
            field_dict["files"] = files
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_teams_file import RESTTeamsFile

        d = dict(src_dict)
        channel_id = d.pop("channelId", UNSET)

        _files = d.pop("files", UNSET)
        files: list[RESTTeamsFile] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = RESTTeamsFile.from_dict(files_item_data)

                files.append(files_item)

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        subject = d.pop("subject", UNSET)

        text = d.pop("text", UNSET)

        rest_files_send_options = cls(
            channel_id=channel_id,
            files=files,
            from_=from_,
            to=to,
            subject=subject,
            text=text,
        )

        rest_files_send_options.additional_properties = d
        return rest_files_send_options

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
