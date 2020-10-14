
import json
import os

from euchrecli.util.env_util import os_file_paths

defaults = {
    'name': '',
    'call-them-bowers': False,
    'styled-output': True
}


def config_init(config_path: str) -> None:
    """Initialize and check euchre-cli user configuration file.
    """
    # create config directory
    if not os.path.exists(config_path):
        os.makedirs(config_path)

    # create config file
    if not os.path.isfile(config_path + 'config.json'):
        with open(config_path + 'config.json', 'w') as fp:
            json.dump(defaults, fp, indent=4)
    else:
        # TODO: check that existing config is valid
        pass


def read_config_file():
    config_path, _ = os_file_paths()

    with open(config_path + 'config.json', 'r') as fp:
        data = fp.read()

    conf = json.loads(data)

    return conf


def update_config_file(conf: dict) -> None:
    config_path, _ = os_file_paths()

    with open(config_path + 'config.json', 'w') as fp:
        json.dump(conf, fp, indent=4)


def get_defaults_configs() -> dict:
    return defaults


def get_config_value(key: str) -> str:
    pass
