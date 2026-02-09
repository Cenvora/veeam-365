from enum import Enum


class RESTCredentialToSendAccountType(str, Enum):
    AMAZONS3ACCOUNT = "amazonS3Account"
    AMAZONS3COMPATIBLEACCOUNT = "amazonS3CompatibleAccount"
    AZUREBLOBACCOUNT = "azureBlobAccount"

    def __str__(self) -> str:
        return str(self.value)
