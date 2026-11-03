from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTRestoreSessionEventType(str, Enum):
    EXPORT = "Export"
    NONE = "None"
    RESTORE = "Restore"
    SAVE = "Save"
    SEND = "Send"
    VIEW = "View"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
