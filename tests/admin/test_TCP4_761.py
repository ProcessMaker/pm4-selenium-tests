#!/usr/local/bin/python3

# Check if using local environment
from os import getenv
if getenv('ENVIRONMENT') == 'local':
    import sys
    from sys import path
    path.append('../../includes')
    from __init__ import data

from test_parent import BaseTest
import util
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
import unittest

class TCP4_761(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_create_user(self):
        ''' Create user with special characters '''
        
        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to admin.
        self.log.append('Step 2: Go to Admin')
        pageMenu.goto_admin()

        # STEP 3: Create User with special character
        # print('Step 3: Create User with special character')
        user_data = pageUser.create_user()

        # STEP 4: Go to Admin
        # print('Step 4: Go to Admin')
        pageMenu.goto_admin()

        # STEP 5: Verify if the user was created
        try:
            # print('Step 5: Verify if the user was created')
            user_result_search = pageUser.search_user(user_data['user_username'])

            self.assertTrue(user_result_search!=None)
            # print('User was found')
        except AssertionError as e:
            raise Exception('Error in search_user function',e)
            # print('User was not found, an error ocurred')

        # print('Create User Test completed')


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_761, data, __main__)