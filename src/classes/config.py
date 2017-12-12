import configparser
from src.classes.logging import Logging

class Config:

    """
    Class responsible for reading the configurations file
    """

    def __init__(self):

        self.log = Logging("Config")

        self.config_parser = configparser.SafeConfigParser()
        self.read_file()


    def read_file(self):
        """
        Read the content of the configurations file
        """
        try:
            self.config_parser.read("src/config.ini")

        except configparser.Error as err:
            self.log.error(err)


    def get(self, section):
        """
        Return the specified section of the configurations file
        as a dict
        """
        try:
            return self.config_parser._sections[section]

        except configparser.Error as err:
            self.log.error(err)
            return []
