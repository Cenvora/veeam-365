from enum import Enum

from ..._lenient_enum import keep_unknown_value


class AmazonS3AwsRegionType(str, Enum):
    CHINA = "China"
    GLOBAL = "Global"
    USGOVERNMENT = "USGovernment"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
