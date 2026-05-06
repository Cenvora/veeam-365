from enum import Enum

class RESTRestoreListConfigDocumentVersion(str, Enum):
    ALL = "All"
    LAST = "Last"

    def __str__(self) -> str:
        return str(self.value)
