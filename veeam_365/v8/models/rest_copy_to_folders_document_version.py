from enum import Enum

class RESTCopyToFoldersDocumentVersion(str, Enum):
    ALL = "All"
    LAST = "Last"

    def __str__(self) -> str:
        return str(self.value)
