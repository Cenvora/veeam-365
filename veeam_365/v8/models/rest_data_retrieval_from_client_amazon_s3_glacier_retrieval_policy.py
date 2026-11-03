from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy(str, Enum):
    BULK = "Bulk"
    EXPEDITED = "Expedited"
    STANDARD = "Standard"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
