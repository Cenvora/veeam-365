from enum import Enum

class RESTCopyToFoldersOfficeRegion(str, Enum):
    CHINA = "China"
    GERMANY = "Germany"
    USDEFENCE = "USDefence"
    USGOVERNMENT = "USGovernment"
    WORLDWIDE = "Worldwide"

    def __str__(self) -> str:
        return str(self.value)
