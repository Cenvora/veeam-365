from enum import Enum

class RESTDataRetrievalFromClientAmazonS3GlacierRetrievalPolicy(str, Enum):
    BULK = "Bulk"
    EXPEDITED = "Expedited"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
