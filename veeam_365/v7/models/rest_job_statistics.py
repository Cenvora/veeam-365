from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rest_job_statistics_bottleneck import RESTJobStatisticsBottleneck
from ..types import UNSET, Unset

T = TypeVar("T", bound="RESTJobStatistics")


@_attrs_define
class RESTJobStatistics:
    """
    Attributes:
        processing_rate_bytes_ps (int | Unset): Average speed of data processing. This counter is a ratio between the
            amount of data that has actually been read and job duration. The value is given in bytes per second.
        processing_rate_items_ps (int | Unset): Average speed of data processing. This counter is a ratio between the
            amount of data that has actually been read and job duration. The value is given in items per second.
        read_rate_bytes_ps (int | Unset): Average speed of reading data from the backup repository. The value is given
            in bytes per second.
        write_rate_bytes_ps (int | Unset): Average speed of writing data to the backup repository. The value is given in
            bytes per second.
        transferred_data_bytes (int | Unset): Amount of data transferred from the source-side to the target-side after
            applying compression and deduplication. The value is given in bytes per second.
        processed_objects (int | Unset): Number of items processed by the backup or backup copy job.
        bottleneck (RESTJobStatisticsBottleneck | Unset): Bottleneck in the data transmission process.
    """

    processing_rate_bytes_ps: int | Unset = UNSET
    processing_rate_items_ps: int | Unset = UNSET
    read_rate_bytes_ps: int | Unset = UNSET
    write_rate_bytes_ps: int | Unset = UNSET
    transferred_data_bytes: int | Unset = UNSET
    processed_objects: int | Unset = UNSET
    bottleneck: RESTJobStatisticsBottleneck | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processing_rate_bytes_ps = self.processing_rate_bytes_ps

        processing_rate_items_ps = self.processing_rate_items_ps

        read_rate_bytes_ps = self.read_rate_bytes_ps

        write_rate_bytes_ps = self.write_rate_bytes_ps

        transferred_data_bytes = self.transferred_data_bytes

        processed_objects = self.processed_objects

        bottleneck: str | Unset = UNSET
        if not isinstance(self.bottleneck, Unset):
            bottleneck = self.bottleneck.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processing_rate_bytes_ps is not UNSET:
            field_dict["processingRateBytesPS"] = processing_rate_bytes_ps
        if processing_rate_items_ps is not UNSET:
            field_dict["processingRateItemsPS"] = processing_rate_items_ps
        if read_rate_bytes_ps is not UNSET:
            field_dict["readRateBytesPS"] = read_rate_bytes_ps
        if write_rate_bytes_ps is not UNSET:
            field_dict["writeRateBytesPS"] = write_rate_bytes_ps
        if transferred_data_bytes is not UNSET:
            field_dict["transferredDataBytes"] = transferred_data_bytes
        if processed_objects is not UNSET:
            field_dict["processedObjects"] = processed_objects
        if bottleneck is not UNSET:
            field_dict["bottleneck"] = bottleneck

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        processing_rate_bytes_ps = d.pop("processingRateBytesPS", UNSET)

        processing_rate_items_ps = d.pop("processingRateItemsPS", UNSET)

        read_rate_bytes_ps = d.pop("readRateBytesPS", UNSET)

        write_rate_bytes_ps = d.pop("writeRateBytesPS", UNSET)

        transferred_data_bytes = d.pop("transferredDataBytes", UNSET)

        processed_objects = d.pop("processedObjects", UNSET)

        _bottleneck = d.pop("bottleneck", UNSET)
        bottleneck: RESTJobStatisticsBottleneck | Unset
        if isinstance(_bottleneck, Unset):
            bottleneck = UNSET
        else:
            bottleneck = RESTJobStatisticsBottleneck(_bottleneck)

        rest_job_statistics = cls(
            processing_rate_bytes_ps=processing_rate_bytes_ps,
            processing_rate_items_ps=processing_rate_items_ps,
            read_rate_bytes_ps=read_rate_bytes_ps,
            write_rate_bytes_ps=write_rate_bytes_ps,
            transferred_data_bytes=transferred_data_bytes,
            processed_objects=processed_objects,
            bottleneck=bottleneck,
        )

        rest_job_statistics.additional_properties = d
        return rest_job_statistics

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
