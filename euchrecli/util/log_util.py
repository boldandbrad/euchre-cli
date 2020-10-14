
import getpass
import os
import platform

from loguru import logger


def logger_init(log_path: str) -> None:
    """Configure loguru logger.
    """
    logger.remove()  # remove stdout/stderr logging since this is a CLI

    log_format = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'

    logger.add(
        log_path, format=log_format, compression='zip', retention='1 day'
    )
