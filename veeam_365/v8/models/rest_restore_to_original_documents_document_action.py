from enum import Enum


class RESTRestoreToOriginalDocumentsDocumentAction(str, Enum):
    KEEP = "Keep"
    OVERWRITE = "Overwrite"

    def __str__(self) -> str:
        return str(self.value)
