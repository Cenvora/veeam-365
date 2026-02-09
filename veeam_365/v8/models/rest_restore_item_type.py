from enum import Enum


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

    def __str__(self) -> str:
        return str(self.value)
