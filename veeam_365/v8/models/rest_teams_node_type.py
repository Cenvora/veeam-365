from enum import Enum


class RESTTeamsNodeType(str, Enum):
    FILES = "Files"
    POSTS = "Posts"
    TABS = "Tabs"

    def __str__(self) -> str:
        return str(self.value)
