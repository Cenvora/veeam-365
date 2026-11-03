"""Let generated enums accept values their OpenAPI schema does not list.

The REST API does not keep a version's enums fixed. A patched server returns values that
appeared after a schema was published, even on the older API versions it still serves: VB365
8.6 sends ``"LibraryItem"`` through v7's ``RESTSharePointFolderType``, and ``"DocumentSet"``
has turned up where no schema lists it. A generated enum raises ValueError on such a value,
which takes down the whole response it sits in, when the caller usually wanted a different
field of it.

``keep_unknown_value`` is installed as ``_missing_`` on every generated enum by
``patch_enums.py``, so an unknown string becomes a member carrying the raw value instead of
an error. It is still an instance of the enum and of ``str``, compares equal to the raw
string, and serializes back unchanged. Known values are unaffected: Enum only consults
``_missing_`` after a lookup by value fails.
"""

from __future__ import annotations

from enum import Enum
from typing import TypeVar

E = TypeVar("E", bound=Enum)


def keep_unknown_value(cls: type[E], value: object) -> E | None:
    """Build a member for a value the schema does not list.

    Returns None for anything that is not a string, so Enum raises its usual ValueError:
    every generated enum is a str enum, and a non-string there is a genuine type error rather
    than a newer server.
    """
    if not isinstance(value, str):
        return None

    member = str.__new__(cls, value)
    member._name_ = value
    member._value_ = value
    return member
