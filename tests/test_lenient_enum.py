"""Tests for enums accepting values their schema does not list.

The motivating case: VB365 8.6 returns "LibraryItem" as a SharePoint item type through the
v7 API, whose schema only knows LibraryFolder and ListFolder, and "DocumentSet" appears where
no schema lists it. Either used to make RESTItemComposed.from_dict raise.
"""

import importlib
import inspect
from enum import Enum

import pytest

from veeam_365.versions import VERSION_TO_PACKAGE

ITEM = {
    "id": "item-1",
    "name": "Shared Documents",
    "createdBy": "admin@example.com",
    "modifiedBy": "admin@example.com",
    "creationTime": "2026-11-01T09:00:00Z",
    "modificationTime": "2026-11-02T09:00:00Z",
}


def models(version):
    return importlib.import_module(f"{VERSION_TO_PACKAGE[version]}.models")


@pytest.mark.parametrize("version", ["v7", "v8"])
@pytest.mark.parametrize("item_type", ["LibraryItem", "DocumentSet"])
def test_item_composed_parses_unlisted_type(version, item_type):
    m = models(version)
    item = m.RESTItemComposed.from_dict({**ITEM, "type": item_type})

    assert isinstance(item.type_, m.RESTSharePointFolderType)
    assert item.type_ == item_type
    assert item.type_.value == item_type
    assert str(item.type_) == item_type
    assert item.to_dict()["type"] == item_type


@pytest.mark.parametrize("version", ["v7", "v8"])
def test_known_value_is_the_real_member(version):
    folder_type = models(version).RESTSharePointFolderType

    assert folder_type("LibraryFolder") is folder_type.LIBRARYFOLDER


def test_unknown_value_does_not_become_a_member():
    folder_type = models("v7").RESTSharePointFolderType
    folder_type("LibraryItem")

    assert "LibraryItem" not in {member.value for member in folder_type}


def test_non_string_still_raises():
    with pytest.raises(ValueError):
        models("v8").RESTSharePointFolderType(3)


@pytest.mark.parametrize("version", sorted(VERSION_TO_PACKAGE))
def test_every_generated_enum_is_lenient(version):
    m = models(version)
    enums = [
        obj
        for _, obj in inspect.getmembers(m, inspect.isclass)
        if issubclass(obj, Enum) and obj.__module__.startswith(m.__name__)
    ]

    assert enums
    for enum_cls in enums:
        assert enum_cls("NotInAnySchema").value == "NotInAnySchema", enum_cls.__name__
