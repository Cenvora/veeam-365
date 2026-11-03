from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTAccountToSendAccountType(str, Enum):
    AMAZONS3ACCOUNT = "amazonS3Account"
    AMAZONS3COMPATIBLEACCOUNT = "amazonS3CompatibleAccount"
    AZUREBLOBACCOUNT = "azureBlobAccount"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
