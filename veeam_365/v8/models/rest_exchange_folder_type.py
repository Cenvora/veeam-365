from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTExchangeFolderType(str, Enum):
    APPOINTMENT = "Appointment"
    CONTACT = "Contact"
    JOURNAL = "Journal"
    NONE = "None"
    STICKYNOTE = "StickyNote"
    TASK = "Task"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
