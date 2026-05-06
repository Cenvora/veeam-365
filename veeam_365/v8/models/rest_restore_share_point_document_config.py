from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_restore_share_point_document_config_document_version import RESTRestoreSharePointDocumentConfigDocumentVersion
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_share_point_document import RESTSharePointDocument





T = TypeVar("T", bound="RESTRestoreSharePointDocumentConfig")



@_attrs_define
class RESTRestoreSharePointDocumentConfig:
    """ 
        Attributes:
            document (RESTSharePointDocument):
            document_version (RESTRestoreSharePointDocumentConfigDocumentVersion | Unset): Specifies what version of the
                SharePoint document will be restored.
     """

    document: RESTSharePointDocument
    document_version: RESTRestoreSharePointDocumentConfigDocumentVersion | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_share_point_document import RESTSharePointDocument
        document = self.document.to_dict()

        document_version: str | Unset = UNSET
        if not isinstance(self.document_version, Unset):
            document_version = self.document_version.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "document": document,
        })
        if document_version is not UNSET:
            field_dict["documentVersion"] = document_version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_share_point_document import RESTSharePointDocument
        d = dict(src_dict)
        document = RESTSharePointDocument.from_dict(d.pop("document"))




        _document_version = d.pop("documentVersion", UNSET)
        document_version: RESTRestoreSharePointDocumentConfigDocumentVersion | Unset
        if isinstance(_document_version,  Unset):
            document_version = UNSET
        else:
            document_version = RESTRestoreSharePointDocumentConfigDocumentVersion(_document_version)




        rest_restore_share_point_document_config = cls(
            document=document,
            document_version=document_version,
        )


        rest_restore_share_point_document_config.additional_properties = d
        return rest_restore_share_point_document_config

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
