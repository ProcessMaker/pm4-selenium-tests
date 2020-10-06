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

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Step 1: Load Login page////////////////')
        self.driver.get(data['server_url'])
        self.driver = PageLogin(self.driver, data).login()


    def test_create_user(self):
        ''' Create user with special characters '''
        # Constants
        self.user_data = {}  # To save user data, when you create an user
        self.user_result_search = None  # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 2: Go to admin.
        self.log.append('Step 2: Go to Admin////////////////')
        pageMenu.goto_admin()

        # STEP 3: Create User with special character
        # print('Step 3: Create User with special character')
        self.log.append('Step 3: Creates an user with a special character////////////////')
        self.user_data = pageUser.create_user()

        # STEP 4: Go to Admin
        # print('Step 4: Go to Admin')
        self.log.append('Step 4: Go to admin////////////////')
        pageMenu.goto_admin()

        # STEP 5: Verify if the user was created
        try:
            # print('Step 5: Verify if the user was created')
            self.log.append('Step 3: Verify if the user was created////////////////')
            self.user_result_search = pageUser.search_user(self.user_data['user_username'])

            self.assertTrue(self.user_result_search is not None)
            # print('User was found')
        except AssertionError as e:
            raise Exception('Error in search_user function', e)
            # print('User was not found, an error ocurred')

        # print('Create User Test completed')

    def tearDown(self):
        ''' Method to run after each test method. '''
        # STEP 6: Deleted user created.
        self.log.append('Step 6: Delete created user////////////////')
        PageUsers(self.driver, data).delete_user(self.user_result_search)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_761, data, __main__)