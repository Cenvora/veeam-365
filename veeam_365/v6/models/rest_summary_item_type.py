from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTSummaryItemType(str, Enum):
    CHANNEL = "Channel"
    FILE = "File"
    POST = "Post"
    POSTSTAB = "PostsTab"
    TAB = "Tab"
    TEAM = "Team"
    TEAMAPP = "TeamApp"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
