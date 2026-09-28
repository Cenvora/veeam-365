from enum import Enum


class AmazonS3AwsRegionType(str, Enum):
    CHINA = "China"
    GLOBAL = "Global"
    USGOVERNMENT = "USGovernment"

    def __str__(self) -> str:
        return str(self.value)
