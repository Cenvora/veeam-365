from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.rest_exception_info_error_code import RESTExceptionInfoErrorCode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RESTExceptionInfo")



@_attrs_define
class RESTExceptionInfo:
    """ 
        Attributes:
            message (str | Unset): Error message.
            error_code (RESTExceptionInfoErrorCode | Unset): Error code.
            stack_trace (None | str | Unset): Error stack trace.
     """

    message: str | Unset = UNSET
    error_code: RESTExceptionInfoErrorCode | Unset = UNSET
    stack_trace: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        error_code: str | Unset = UNSET
        if not isinstance(self.error_code, Unset):
            error_code = self.error_code.value


        stack_trace: None | str | Unset
        if isinstance(self.stack_trace, Unset):
            stack_trace = UNSET
        else:
            stack_trace = self.stack_trace


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if stack_trace is not UNSET:
            field_dict["stackTrace"] = stack_trace

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _error_code = d.pop("errorCode", UNSET)
        error_code: RESTExceptionInfoErrorCode | Unset
        if isinstance(_error_code,  Unset):
            error_code = UNSET
        else:
            error_code = RESTExceptionInfoErrorCode(_error_code)




        def _parse_stack_trace(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stack_trace = _parse_stack_trace(d.pop("stackTrace", UNSET))


        rest_exception_info = cls(
            message=message,
            error_code=error_code,
            stack_trace=stack_trace,
        )


        rest_exception_info.additional_properties = d
        return rest_exception_info

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
