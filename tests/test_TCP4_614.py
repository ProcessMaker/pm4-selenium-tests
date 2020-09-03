#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../includes')
    # Import __init__ to include data configuration
    from __init__ import data


from test_parent import BaseTest
from util import run_test
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
from page_user_information import PageUserInformation

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TCP4_614(BaseTest):
    ''' Test that the country of an user can be changed '''

    def test_tcp4_614(self):
        '''Edits an users country'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Redirect to Admin Users page, wait for +User button to be clickable 
        PageMenu(self.driver, data).goto_admin()

        # Wait for user edit form to load, changes the country and save
        PageUsers(self.driver, data).edit_non_admin()
        PageUserInformation(self.driver, data).change_user_country('bolivia')

        # Gets the text from the selected option and confirms it changed
        PageMenu(self.driver, data).goto_admin()
        PageUsers(self.driver, data).edit_non_admin()
        self.assertTrue(PageUserInformation(self.driver, self.data).confirm_country("bolivia"))


if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_614, data, __main__)
