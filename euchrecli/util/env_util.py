
import getpass
import os
import platform


def os_file_paths() -> (str, str):
    is_travis = 'TRAVIS' in os.environ  # running in travis ci
    usrname = getpass.getuser()

    if platform.system() == 'Linux' and not is_travis:
        config_path = f'/home/{usrname}/.euchre-cli/'
        log_path = '/var/log/euchre-cli/euchre.log'
    elif platform.system() == 'Darwin' and not is_travis:
        config_path = f'/Users/{usrname}/.euchre-cli/'
        log_path = f'/Users/{usrname}/Library/Logs/euchre-cli/euchre.log'
    elif platform.system() == 'Windows' and not is_travis:
        config_path = f'C:\\Users\\{usrname}\\.euchre-cli\\'
        log_path = \
            f'C:\\Users\\{usrname}\\AppData\\local\\euchre-cli\\euchre.log'
    else:
        config_path = 'config.json'
        log_path = 'euchre.log'

    return config_path, log_path
