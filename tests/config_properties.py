"""
LayConf - Layered Configuration Parser for Python3
Written by david.ohana@ibm.com
License: Apache-2.0

get config string
myConfig = Config.get("LOG", "file_backup_count")

get all section key values
log_section = Config.getsection("DEFAULT")
sectionValue = log_section["env_name"]
"""

import configparser
import os


class Config:
    _config_parser_default = configparser.ConfigParser()
    _config_parser_custom = configparser.ConfigParser()
    env_prefix = ""

    ERROR_WHEN_NOT_FOUND = object
    BOOLEAN_STATES = {'1': True, 'yes': True, 'true': True, 'on': True,
                      '0': False, 'no': False, 'false': False, 'off': False}

    @staticmethod
    def init_config(default_config_file_path="config/default.ini", custom_config_file_path="", env_prefix=""):
        assert not is_none_or_blank(default_config_file_path)
        if env_prefix is None:
            env_prefix = ""

        Config.env_prefix = env_prefix
        Config._config_parser_default.read(default_config_file_path)
        if not is_none_or_blank(custom_config_file_path):
            Config._config_parser_custom.read(custom_config_file_path)

        print("config env prefix:", env_prefix)
        print("config default:", default_config_file_path)
        print("config custom:", custom_config_file_path)

    @staticmethod
    def get(*args):
        if len(args) == 1:
            section = "DEFAULT"
            option = ''.join(args[0])
        else:
            section = ''.join(args[0])
            option = ''.join(args[1])
        assert not is_none_or_blank(section)
        assert not is_none_or_blank(option)

        env_key = Config._get_env_key(section, option)
        env_val = os.environ.get(env_key)
        if env_val is not None:
            return env_val

        custom_val = Config._config_parser_custom.get(section, option, fallback=None)
        if custom_val is not None:
            return custom_val

        default_val = Config._config_parser_default.get(section, option, fallback=None)
        if default_val is not None:
            return default_val

        raise KeyError(f"Configuration value for {section}/{option} not found")

    @staticmethod
    def getint(*args):
        str_value = Config.get(args)
        return int(str_value)

    @staticmethod
    def getfloat(*args):
        str_value = Config.get(args)
        return float(str_value)

    @staticmethod
    def getboolean(*args):
        str_value = Config.get(args)
        return Config._convert_to_boolean(str_value)

    @staticmethod
    def getsection(section: str):
        assert not is_none_or_blank(section)
        return Section(section)

    @staticmethod
    def _get_env_key(section, option):
        tokens = []
        if Config.env_prefix:
            tokens.append(Config.env_prefix)
        if section != 'DEFAULT':
            tokens.append(section)
        tokens.append(option)
        return '_'.join(tokens)

    @staticmethod
    def _convert_to_boolean(value):
        """Return a boolean value translating from other types if necessary.
        """
        if value.lower() not in Config.BOOLEAN_STATES:
            raise ValueError('Not a boolean: %s' % value)
        return Config.BOOLEAN_STATES[value.lower()]


def is_none_or_blank(s: str):
    return s is None or str(s) == ""

class Section:
    def __init__(self, section: str):
        self.section = section

    def __getitem__(self, option: str):
        return Config.get(self.section, option)

    def get(self, option: str):
        return Config.get(self.section, option)

    def getint(self, option: str):
        return Config.getint(self.section, option)

    def getfloat(self, option: str):
        return Config.getfloat(self.section, option)

    def getboolean(self, option: str):
        return Config.getboolean(self.section, option)

