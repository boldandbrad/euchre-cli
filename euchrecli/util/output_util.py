
import time


def _wait(delay: float):
    """Pause thread execution for a duration in seconds.

    Args:
        delay (int, optional): Seconds to pause.
    """
    time.sleep(delay)


def output(message: str, delay: float = 1.25):
    """Print out a message to the user after pausing for a duration in seconds.

    Args:
        message (str): Message to be printed out
        delay (float, optional): Seconds to pause. Defaults to 1.25.
    """
    _wait(delay)
    print(message)
