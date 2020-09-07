#!/usr/local/bin/python3

# Check if using local environment
from os import getenv
if getenv('ENVIRONMENT') == 'local':
    from sys import path
    path.append('../../includes')
    from __init__ import data

from test_parent import BaseTest
import util
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
import unittest

class TCP4_762(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_create_user(self):
        ''' Create user with special characters '''
        #Constants
        data_user = {'password': 'Co1054!"·$%&/()='}
        print('message')

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
        #
        # # STEP 3: Fill the user data with special character
        # try:
        #     self.log.append('Step 3: Create User with special character')
        #     result = pageUser.create_user_data(data_user)
        #     self.assertIn('The user was successfully created',result.text)
        #     self.log.append('The user was successfully created')
        # except AssertionError as e:
        #     self.log.append('User could not be created, an error occurred')
        #     self.assertionFailures.append(str(e))
        print('dfdf')
        pageUser.search_user('admin')





if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_762, data, __main__)
