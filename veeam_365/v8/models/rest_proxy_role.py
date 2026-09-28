from enum import Enum


class RESTProxyRole(str, Enum):
    APPLIANCEPROCESSOR = "ApplianceProcessor"
    ORCHESTRATOR = "Orchestrator"
    PROCESSOR = "Processor"
    SCHEDULER = "Scheduler"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
