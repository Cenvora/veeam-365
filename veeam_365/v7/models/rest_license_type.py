from enum import Enum


class RESTLicenseType(str, Enum):
    AWSPRIVATEOFFER = "AwsPrivateOffer"
    COMMUNITY = "Community"
    EVALUATION = "Evaluation"
    NFR = "NFR"
    RENTAL = "Rental"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
