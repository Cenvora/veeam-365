from enum import Enum


class RESTCopyToDocumentDocumentLastVersionAction(str, Enum):
    MERGE = "Merge"
    OVERWRITE = "Overwrite"

    def __str__(self) -> str:
        return str(self.value)
