from enum import Enum


class RESTDataRetrievalFromClientAzureArchiveRetrievalPolicy(str, Enum):
    HIGHPRIORITY = "HighPriority"
    STANDARDPRIORITY = "StandardPriority"

    def __str__(self) -> str:
        return str(self.value)
