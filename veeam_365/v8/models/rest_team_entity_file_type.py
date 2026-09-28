from enum import Enum


class RESTTeamEntityFileType(str, Enum):
    FILE = "File"
    FOLDER = "Folder"

    def __str__(self) -> str:
        return str(self.value)
