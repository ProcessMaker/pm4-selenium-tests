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
from page_user_information import PageUserInformation
import unittest

class TCP4_763(BaseTest):
    ''' Test to verify that a user was deleted '''

    def test_delete_user(self):
        ''' Create user with Complete User information '''
        #Constants
        user_data = {}              # To save user data, when you create an user
        user_result_search = None   # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)
        pageUserInformation = PageUserInformation(self.driver, data)

        # STEP 1: Load login page.
        # print('Step 1: Load Login page')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to admin.
        # print('Step 2: Go to Admin')
        pageMenu.goto_admin()

        # STEP 3: Create User
        # print('Step 3: Create User')
        user_data = pageUser.create_user()

        # STEP 4: Go to admin.
        # print('Step 4: Go to Admin')
        pageMenu.goto_admin()

        # STEP 5: Search user created.
        # print('STEP 5: Search user created.')
        try:
            user_result_search = pageUser.search_user(user_data['user_username'])
            self.assertTrue(user_result_search != None)
        except AssertionError as e:
            raise Exception('Error in search_user function',e)

        # STEP 6: Deleted user created.
        # print('STEP 6: Delete user created before.')
        pageUser.delete_user(user_result_search)

        # STEP 7: Go to admin.
        # print('Step 7: Go to Admin')
        pageMenu.goto_admin()

        # STEP 8: Verify deleted user.
        # print('STEP 8: Delete user created before.')
        try:
            user_result_search = pageUser.search_user(user_data['user_username'])
            self.assertTrue(user_result_search == None)
            # print('User was deleted successfully')
        except AssertionError as e:
            raise Exception('Error in delete_user function',e)

        # print('Deleted user Test completed')

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_763, data, __main__)