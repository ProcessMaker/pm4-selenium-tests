#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../../includes')
    # Import __init__ to include data configuration
    from __init__ import data
# Import BaseTest class where webdriver instance is created
from test_parent import BaseTest
# Import util file where all helper functions are located
import util
# Import all page classes
from page import *
# Import Python unittest module
import unittest

from page_login import PageLogin
from page_users import PageUsers
from page_menu import PageMenu


class TCP4_874(BaseTest):
    ''' Verify the login for an active user '''

    def test_tcp4_874(self):
        '''Create user with active status'''
        #Constants
        user_data = {}              # To save user data, when you create an user
        
        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to admin.
        self.log.append('Step 2: Go to Admin')
        pageMenu.goto_admin()

        # STEP 3: Create an active User
        self.log.append('Step 3: Create an active User')
        
        user_data = pageUser.create_user()

        # STEP 4: Log out as Admin user
        self.log.append('STEP 4: Log out as Admin user')
        pageMenu.log_out()

        # STEP 5: Log in with a new user with status active
        try:
            self.log.append('STEP 5: Log in with a new user with status active')
            myPage = login_page.loginNoAdmin(user_data['user_username'], user_data['user_password'])
            self.assertEqual(myPage.current_url,data['server_url'] + '/login')
        except AssertionError as e:
            raise Exception('Error in loginNoAdmin function',e)

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_874, data, __main__)