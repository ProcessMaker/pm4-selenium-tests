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

import unittest
import time
from util import run_test
from test_parent import BaseTest
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
from page_user_information import PageUserInformation

class TCP4_623(BaseTest):
    ''' Test that the timezone of an user can be changed '''

    def test_tcp4_623(self):
        '''Edits an users timezone'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Redirect to Admin Users page, wait for +User button to be clickable 
        PageMenu(self.driver, data).goto_admin()
        
        # Find table record with ID != '1', find edit button in this element, and click
        PageUsers(self.driver, data).edit_non_admin()

        # Changes the timezone of the selected user
        PageUserInformation(self.driver, self.data).change_user_timezone("africa")

        # refresh the user details page
        PageMenu(self.driver, data).goto_admin()
        PageUsers(self.driver, data).edit_non_admin()

        # Gets the text from the selected option and confirms it changed
        self.assertTrue(PageUserInformation(self.driver, self.data).confirm_timezone("africa"))

if __name__ == "__main__":
    import __main__  
    output = run_test(TCP4_623, data, __main__)