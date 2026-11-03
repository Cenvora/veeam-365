#!/usr/bin/env python3
"""Make generated enums keep values their schema does not list instead of raising.

Usage:
  python patch_enums.py <package dir> [<package dir> ...]

e.g. ``python patch_enums.py veeam_365/v8``. Run after every generation: openapi-python-client
overwrites the models, and this re-applies the change. Already-patched files are left alone,
so it is safe to run repeatedly.

Each ``class X(str, Enum)`` in ``<package dir>/models`` gets
``_missing_ = classmethod(keep_unknown_value)``; see ``veeam_365/_lenient_enum.py`` for why.
"""

import re
import sys
from pathlib import Path

ENUM_CLASS = re.compile(r"^class \w+\(str, Enum\):\n", re.MULTILINE)
IMPORT = "from ..._lenient_enum import keep_unknown_value\n"
HOOK = "    _missing_ = classmethod(keep_unknown_value)\n\n"
STR_METHOD = "    def __str__(self) -> str:\n"


def patch_file(path: Path) -> bool:
    """Patch one model file. Returns True if it changed."""
    text = path.read_text(encoding="utf-8")
    if not ENUM_CLASS.search(text) or "keep_unknown_value" in text:
        return False

    if text.count(STR_METHOD) != 1:
        raise RuntimeError(f"{path}: expected exactly one __str__ to anchor the hook")

    text = text.replace(
        "from enum import Enum\n", f"from enum import Enum\n\n{IMPORT}", 1
    )
    text = text.replace(STR_METHOD, HOOK + STR_METHOD, 1)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__)
        return 2

    for package in argv:
        models = Path(package) / "models"
        if not models.is_dir():
            print(f"{models} is not a directory", file=sys.stderr)
            return 1
        changed = sum(patch_file(path) for path in sorted(models.glob("*.py")))
        print(f"{package}: patched {changed} enum(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
