from enum import Enum

from ..._lenient_enum import keep_unknown_value


class RESTLicenseType(str, Enum):
    AWSPRIVATEOFFER = "AwsPrivateOffer"
    COMMUNITY = "Community"
    EVALUATION = "Evaluation"
    NFR = "NFR"
    RENTAL = "Rental"
    SUBSCRIPTION = "Subscription"

    _missing_ = classmethod(keep_unknown_value)

    def __str__(self) -> str:
        return str(self.value)
