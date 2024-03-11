import os

REDIS_URL = os.getenv(
    "REDIS_URL",
    default="redis://localhost:6379/0",
)

OTHER_URL = os.getenv(
    "OTHER_URL",
    default="",
)

EXCHANGE_URL = os.getenv(
    "EXCHANGE_URL",
    default="",
)
