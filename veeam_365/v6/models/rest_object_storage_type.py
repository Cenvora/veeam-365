from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTObjectStorageType(str, Enum):
    AMAZONS3 = "AmazonS3"
    AMAZONS3COMPATIBLE = "AmazonS3Compatible"
    AMAZONS3GLACIER = "AmazonS3Glacier"
    AZUREBLOB = "AzureBlob"
    AZUREBLOBARCHIVE = "AzureBlobArchive"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
