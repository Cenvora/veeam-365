from enum import Enum

from ..._lenient_enum import keep_unknown_value


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

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
