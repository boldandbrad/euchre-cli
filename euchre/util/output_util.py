
import sys
import time

from loguru import logger


def output(message: str = '', delay: float = 1.25):
    """Print out a message to the user after pausing for a duration in seconds.

    Args:
        message (str): Message to be printed out
        delay (float, optional): Seconds to pause. Defaults to 1.25.
    """
    if 'pytest' not in sys.modules:
        time.sleep(delay)
    print(message)
    logger.debug(message)
