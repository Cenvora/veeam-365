from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTDataRetrievalStorageType(str, Enum):
    AMAZONS3GLACIER = "AmazonS3Glacier"
    AZUREARCHIVE = "AzureArchive"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
