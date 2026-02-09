from enum import Enum


class RESTSummaryItemType(str, Enum):
    CHANNEL = "Channel"
    FILE = "File"
    POST = "Post"
    POSTSTAB = "PostsTab"
    TAB = "Tab"
    TEAM = "Team"
    TEAMAPP = "TeamApp"

    def __str__(self) -> str:
        return str(self.value)
