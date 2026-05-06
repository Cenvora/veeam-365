from enum import Enum

class RESTRestoreListConfigDocumentLastVersionAction(str, Enum):
    MERGE = "Merge"
    OVERWRITE = "Overwrite"

    def __str__(self) -> str:
        return str(self.value)
