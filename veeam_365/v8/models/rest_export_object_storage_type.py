from enum import Enum


class RESTExportObjectStorageType(str, Enum):
    AZUREBLOB = "AzureBlob"

    def __str__(self) -> str:
        return str(self.value)
