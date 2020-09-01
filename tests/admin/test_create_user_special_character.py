#!/usr/local/bin/python3

# Check if using local environment
from sys import path
path.append('../')
from Config import Config
Config.init_config('../config/default.ini')
if Config.get('ENVIRONMENT') == 'local':
    path.append('../../includes')
    data = Config.getsection("DEFAULT")

from test_parent import BaseTest
import util
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
import logging



class TCP4_761(BaseTest):
    ''' Test that the country of an user can be changed '''

    def test_create_user_special_character(self):

        user_data = {'username': 'smoke','firstName': 'test','lastName': 'test qa','jobTitle': 'smoke test','status': 'Active',
                     'email': 'test@processmaker.com','password': 'Co1054!"·$%&/()='}
        self.driver = PageLogin(self.driver, data).login()

        PageMenu(self.driver,data).goto_admin()
        page_user = PageUsers(self.driver,data)

        logging.debug('This is a debug message')
        logging.info('This is an info message')
        logging.warning('This is a warning message')
        logging.error('This is an error message')
        logging.critical('This is a critical message')
        logging.debug('This is a debug message')
        logging.info('This is an info message')

if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_761, data, __main__)
