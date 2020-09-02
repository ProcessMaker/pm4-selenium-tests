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

    def setUp(self):
        #Load server url
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

    def test_correct_login(self):
        #Constants
        data_user = {'password': 'Co1054!"·$%&/()=', 'confPassword': 'Co1054!"·$%&/()='}

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 1: Load login page.
        pageMenu.goto_admin()
        logging.info('Step 1: Go to Admin')

        # STEP 2: Click on the +user button
        logging.info('Step 2: Click +User')

        # STEP 3: Fill the data with special character
        result = pageUser.create_user_data(data_user)
        try:
            self.assertIn('The user was successfully created',result.text)
            logging.info('Step 3: User created with special character')
        except:
            logging.error('Step 3: User could not be created, an error occurred')



if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_761, data, __main__)
