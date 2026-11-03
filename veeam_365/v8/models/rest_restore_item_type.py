from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTRestoreItemType(str, Enum):
    EXCHANGEMAILBOX = "ExchangeMailbox"
    ONEDRIVEITEM = "OneDriveItem"
    SHAREPOINTITEM = "SharePointItem"
    SHAREPOINTLIST = "SharePointList"
    SHAREPOINTSITE = "SharePointSite"
    TEAMSCHANNEL = "TeamsChannel"
    TEAMSFILE = "TeamsFile"
    TEAMSPOST = "TeamsPost"
    TEAMSPOSTSTAB = "TeamsPostsTab"
    TEAMSTAB = "TeamsTab"
    TEAMSTEAM = "TeamsTeam"
    TEAMSTEAMAPP = "TeamsTeamApp"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
