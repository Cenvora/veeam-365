from enum import Enum


class RESTBackupRepositoryFromClientRetentionType(str, Enum):
    ITEMLEVEL = "ItemLevel"
    SNAPSHOTBASED = "SnapshotBased"

    def __str__(self) -> str:
        return str(self.value)
