from enum import Enum

class RESTBackupRepositoryRetentionType(str, Enum):
    ITEMLEVEL = "ItemLevel"
    SNAPSHOTBASED = "SnapshotBased"

    def __str__(self) -> str:
        return str(self.value)
