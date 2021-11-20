
import getpass
import os
import platform

from loguru import logger


def logger_init() -> None:
    """Configure loguru logger.
    """
    logger.remove()  # remove stdout/stderr logging since this is a CLI

    is_travis = 'TRAVIS' in os.environ  # running in travis ci
    usrname = getpass.getuser()

    if platform.system() == 'Linux' and not is_travis:
        log_path = '/var/log/euchre-cli/euchre.log'
    elif platform.system() == 'Darwin' and not is_travis:
        log_path = f'/Users/{usrname}/Library/Logs/euchre-cli/euchre.log'
    elif platform.system() == 'Windows' and not is_travis:
        log_path = \
            f'C:\\Users\\{usrname}\\AppData\\local\\euchre-cli\\euchre.log'
    else:
        log_path = 'euchre.log'

    log_format = '{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}'

    logger.add(
        log_path, format=log_format, compression='zip', retention='1 day'
    )
