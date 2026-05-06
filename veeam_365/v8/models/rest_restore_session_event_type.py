from enum import Enum

class RESTRestoreSessionEventType(str, Enum):
    EXPORT = "Export"
    NONE = "None"
    RESTORE = "Restore"
    SAVE = "Save"
    SEND = "Send"
    VIEW = "View"

    def __str__(self) -> str:
        return str(self.value)
