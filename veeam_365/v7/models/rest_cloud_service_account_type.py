from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTCloudServiceAccountType(str, Enum):
    AWS = "AWS"
    AZURE = "Azure"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
