from enum import Enum


class RESTProxyOperatingSystem(str, Enum):
    LINUX = "Linux"
    WINDOWS = "Windows"

    def __str__(self) -> str:
        return str(self.value)
