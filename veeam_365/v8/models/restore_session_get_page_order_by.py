from enum import Enum


class RestoreSessionGetPageOrderBy(str, Enum):
    CREATIONTIME = "CreationTime"
    ENDTIME = "EndTime"

    def __str__(self) -> str:
        return str(self.value)
