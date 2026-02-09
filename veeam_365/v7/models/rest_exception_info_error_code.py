from enum import Enum


class RESTExceptionInfoErrorCode(str, Enum):
    PROXYOFFLINE = "ProxyOffline"

    def __str__(self) -> str:
        return str(self.value)
