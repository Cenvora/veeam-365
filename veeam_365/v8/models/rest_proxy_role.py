from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTProxyRole(str, Enum):
    APPLIANCEPROCESSOR = "ApplianceProcessor"
    ORCHESTRATOR = "Orchestrator"
    PROCESSOR = "Processor"
    SCHEDULER = "Scheduler"
    UNKNOWN = "Unknown"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
