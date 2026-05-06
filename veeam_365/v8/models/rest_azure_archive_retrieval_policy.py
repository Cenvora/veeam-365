from enum import Enum

class RESTAzureArchiveRetrievalPolicy(str, Enum):
    HIGHPRIORITY = "HighPriority"
    STANDARDPRIORITY = "StandardPriority"

    def __str__(self) -> str:
        return str(self.value)
