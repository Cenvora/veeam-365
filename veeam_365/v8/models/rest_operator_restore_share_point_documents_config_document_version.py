from enum import Enum


class RESTOperatorRestoreSharePointDocumentsConfigDocumentVersion(str, Enum):
    ALL = "All"
    LAST = "Last"

    def __str__(self) -> str:
        return str(self.value)
