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

import util
from test_parent import BaseTest

from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
from page_user_information import PageUserInformation
from __init__ import data

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TCP4_622(BaseTest):
    ''' Test that the date format of an user can be changed '''

    def test_tcp4_622(self):
        '''Edits an users date format'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Redirect to Admin Users page, wait for +User button to be clickable 
        PageMenu(self.driver, self.data).goto_admin()
        
        # Find table record with ID = '2', find edit button in this element, and click
        PageUsers(self.driver, self.data).edit_non_admin()
        
        # Wait for user edit form to load, changes the datetime and save
        PageUserInformation(self.driver, self.data).change_user_datetime("dmyhi")

        # Navigate to Users page and wait for Users table to load then opens the details page
        PageMenu(self.driver, self.data).goto_admin()
        PageUsers(self.driver, self.data).edit_non_admin()

        # Gets the text from the selected option and confirms it changed
        dropdown = Select(self.driver.find_element_by_id('datetime_format'))
        self.assertTrue(PageUserInformation(self.driver, self.data).confirm_datetime("dmyhi"))
        
if __name__ == "__main__":
    import __main__    
    output = util.run_test(TCP4_622, data, __main__)
    print(output)