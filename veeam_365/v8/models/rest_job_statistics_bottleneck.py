from enum import Enum

class RESTJobStatisticsBottleneck(str, Enum):
    DETECTING = "Detecting"
    NA = "NA"
    SOURCE = "Source"
    TARGET = "Target"

    def __str__(self) -> str:
        return str(self.value)
