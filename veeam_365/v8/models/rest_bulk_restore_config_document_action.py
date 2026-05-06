from enum import Enum

class RESTBulkRestoreConfigDocumentAction(str, Enum):
    KEEP = "Keep"
    OVERWRITE = "Overwrite"

    def __str__(self) -> str:
        return str(self.value)
