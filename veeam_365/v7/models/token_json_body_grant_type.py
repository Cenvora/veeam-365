from enum import Enum


class TokenJsonBodyGrantType(str, Enum):
    INTEGRATION = "integration"
    OPERATOR = "operator"
    PASSWORD = "password"
    REFRESH_TOKEN = "refresh_token"
    URNIETFPARAMSOAUTHGRANT_TYPEJWT_BEARER = "urn:ietf:params:oauth:grant-type:jwt-bearer"

    def __str__(self) -> str:
        return str(self.value)
