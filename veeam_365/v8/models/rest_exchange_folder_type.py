from enum import Enum


class RESTExchangeFolderType(str, Enum):
    APPOINTMENT = "Appointment"
    CONTACT = "Contact"
    JOURNAL = "Journal"
    NONE = "None"
    STICKYNOTE = "StickyNote"
    TASK = "Task"

    def __str__(self) -> str:
        return str(self.value)
