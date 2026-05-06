from enum import Enum

class RESTProxyFromClientThrottlingUnit(str, Enum):
    KBS = "KBs"
    MBPS = "Mbps"
    MBS = "MBs"

    def __str__(self) -> str:
        return str(self.value)
