from enum import Enum

class RESTExceptionInfoErrorCode(str, Enum):
    HTTPERROR = "HttpError"
    OPERATIONCONFLICT = "OperationConflict"
    ORGANIZATIONTRANSFER = "OrganizationTransfer"
    OUTDATEDCHANGETOKEN = "OutdatedChangeToken"
    PARAMETERVALIDATIONFAILURE = "ParameterValidationFailure"
    PROXYOFFLINE = "ProxyOffline"
    REPOSITORYOWNERCHANGETOOMANYLINKS = "RepositoryOwnerChangeTooManyLinks"
    RESOURCEACCESSDENIED = "ResourceAccessDenied"
    RESOURCENOTFOUND = "ResourceNotFound"
    TIMEOUT = "Timeout"

    def __str__(self) -> str:
        return str(self.value)
