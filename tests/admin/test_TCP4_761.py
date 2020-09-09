#!/usr/local/bin/python3

# Check if using local environment
import sys
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

class TCP4_761(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_create_user(self):
        ''' Create user with special characters '''
        #Constants
        data_user = {'user_name':'JULIETA','password': 'Co1054!"·$%&/()='}
        user_result_search = None
        result =[]

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageUser = PageUsers(self.driver, data)

        # STEP 1: Load login page.
        print('Step 1: Load Login page', file=sys.stderr)
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to admin.
        print('Step 2: Go to Admin', file=sys.stderr)
        pageMenu.goto_admin()

        # STEP 3: Fill the user data with special character
        try:
            print('Step 3: Create User with special character', file=sys.stderr)
            result = pageUser.create_user_data(data_user)
            self.assertIn('The user was successfully created',result[0])
            print('The user was successfully created', file=sys.stderr)
        except AssertionError as e:
            print('User could not be created, an error occurred', file=sys.stderr)
            self.assertionFailures.append(str(e))

        # STEP 4: Go to Admin
        print('Step 4: Go to Admin', file=sys.stderr)
        pageMenu.goto_admin()

        # STEP 5: Find user Created
        try:
            print('Step 5: Find user created', file=sys.stderr)
            user_result_search = pageUser.search_user(result[1])
            print(user_result_search, file=sys.stderr)
            self.assertTrue(user_result_search!=None)
            print('User was found', file=sys.stderr)
        except AssertionError as e:
            print('User was not found, an error ocurred', file=sys.stderr)
            self.assertionFailures.append(str(e))

        # STEP 6: Delete newly created User
        try:
            print('Step 6: Deleted newly created User', file=sys.stderr)
            print(user_result_search, file=sys.stderr)
            user_deleted = pageUser.delete_user(user_result_search)

            # Verify uf user was deleted
            print('Step 7: Verify user was deleted', file=sys.stderr)
            self.assertIn('The user was deleted', user_deleted.text)
            print('The user was successfully deleted', file=sys.stderr)
        except AssertionError as e:
            print('User was not deleted, an error ocurred', file=sys.stderr)
            self.assertionFailures.append(str(e))






if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_761, data, __main__)
