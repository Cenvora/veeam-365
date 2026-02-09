from enum import Enum


class RESTProxyMaintenanceModeState(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"
    ENABLING = "Enabling"

    def __str__(self) -> str:
        return str(self.value)
