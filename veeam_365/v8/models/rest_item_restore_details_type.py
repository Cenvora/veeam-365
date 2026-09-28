from enum import Enum


class RESTItemRestoreDetailsType(str, Enum):
    BULKMAILBOX = "BulkMailbox"
    BULKONEDRIVE = "BulkOneDrive"
    ITEM = "Item"

    def __str__(self) -> str:
        return str(self.value)
