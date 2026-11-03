from enum import Enum

from ..._lenient_enum import keep_unknown_value


class TokenJsonBodyGrantType(str, Enum):
    OPERATOR = "operator"
    PASSWORD = "password"
    REFRESH_TOKEN = "refresh_token"
    URNIETFPARAMSOAUTHGRANT_TYPEJWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
