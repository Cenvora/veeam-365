from enum import Enum

class RESTHealthStatus(str, Enum):
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"

    def __str__(self) -> str:
        return str(self.value)
