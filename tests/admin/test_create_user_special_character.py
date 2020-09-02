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
import unittest
import time

logging.basicConfig(filename='example.log',level=logging.INFO)

class TCP4_761(BaseTest):

    def test_correct_login(self):
        #Constants
        data_user = {'password': 'Co1054!"·$%&/()=', 'confPassword': 'Co1054!"·$%&/()='}

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 1: Load login page.
        logging.info('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to admin.
        logging.info('Step 2: Go to Admin')
        pageMenu.goto_admin()

        # STEP 3: Fill the user data with special character
        try:
            logging.info('Step 3: Create User with special character')
            result = pageUser.create_user_data(data_user)
            self.assertIn('The user was successfully created',result.text)
        except:
            logging.error('Step 3: User could not be created, an error occurred')



if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_761, data, __main__)
