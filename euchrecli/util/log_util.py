
import getpass
import platform

from loguru import logger


def get_logger() -> logger:
    """Configure and return loguru logger.

    Returns:
        logger: loguru logger
    """
    logger.remove()  # remove std.out/std.err since this is a CLI
    logger.disable('tests')

    username = getpass.getuser()

    if platform.system() == 'Linux':
        log_path = '/var/log/euchre-cli/euchre.log'
    elif platform.system() == 'Darwin':
        log_path = f'/Users/{username}/Library/Logs/euchre-cli/euchre.log'
    elif platform.system() == 'Windows':
        log_path = \
            f'C:\\Users\\{username}\\AppData\\local\\euchre-cli\\euchre.log'

    log_format = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'

    logger.add(
        log_path, format=log_format, compression='zip', retention='1 day'
    )
    return logger
