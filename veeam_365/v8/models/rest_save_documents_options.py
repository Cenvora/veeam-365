from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.rest_one_drive_document import RESTOneDriveDocument





T = TypeVar("T", bound="RESTSaveDocumentsOptions")



@_attrs_define
class RESTSaveDocumentsOptions:
    """ 
        Attributes:
            documents (list[RESTOneDriveDocument] | Unset): Specifies IDs of the OneDrive documents that you want to save.
                For more information on how to get such IDs, see [Get OneDrive
                Documents](#/OneDriveDocument/OneDriveDocument_Get).
     """

    documents: list[RESTOneDriveDocument] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.rest_one_drive_document import RESTOneDriveDocument
        documents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rest_one_drive_document import RESTOneDriveDocument
        d = dict(src_dict)
        _documents = d.pop("documents", UNSET)
        documents: list[RESTOneDriveDocument] | Unset = UNSET
        if _documents is not UNSET:
            documents = []
            for documents_item_data in _documents:
                documents_item = RESTOneDriveDocument.from_dict(documents_item_data)



                documents.append(documents_item)


        rest_save_documents_options = cls(
            documents=documents,
        )


        rest_save_documents_options.additional_properties = d
        return rest_save_documents_options

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
