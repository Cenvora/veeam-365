from enum import Enum


class RESTDataRetrievalStorageType(str, Enum):
    AMAZONS3GLACIER = "AmazonS3Glacier"
    AZUREARCHIVE = "AzureArchive"

    def __str__(self) -> str:
        return str(self.value)
