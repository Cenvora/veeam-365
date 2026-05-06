from enum import Enum

class RESTProxyThrottlingUnit(str, Enum):
    KBS = "KBs"
    MBPS = "Mbps"
    MBS = "MBs"

    def __str__(self) -> str:
        return str(self.value)
