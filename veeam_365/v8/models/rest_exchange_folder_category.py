from enum import Enum


class RESTExchangeFolderCategory(str, Enum):
    CONFLICTS = "Conflicts"
    DELETED = "Deleted"
    DISCOVERYHOLDS = "DiscoveryHolds"
    DRAFTS = "Drafts"
    INBOX = "Inbox"
    JUNK = "Junk"
    LOCALFAILURES = "LocalFailures"
    NONE = "None"
    OUTBOX = "Outbox"
    PERMANENTLYDELETEDITEMS = "PermanentlyDeletedItems"
    PURGES = "Purges"
    SENT = "Sent"
    SERVERFAILURES = "ServerFailures"
    SYNCISSUES = "SyncIssues"
    TEAMSMESSAGESDATA = "TeamsMessagesData"
    VERSIONS = "Versions"

    def __str__(self) -> str:
        return str(self.value)
