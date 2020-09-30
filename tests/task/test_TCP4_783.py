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
from page_request import PageRequest
from page_new_savedsearch import PageNewSavedsearch
from page_lateral_request import PageLateralRequest
from page_savedsearch import PageSavedsearch


from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TCP4_783(BaseTest):
    ''' Test that a new saved search can be created'''

    def test_tcp4_783(self):
        '''Creates a new saved search'''

        # Login using configured url, workspace, username, and password
        self.log.append('Step 1: Load Login page////////////////')
        self.driver = PageLogin(self.driver, data).login()

        # Redirect to Admin Users page, wait for +User button to be clickable
        self.log.append('Step 2: Go to request////////////////')
        PageMenu(self.driver, data).goto_request()

        # Creates a saved search
        self.log.append('Step 3: Creates a saved search////////////////')
        PageRequest(self.driver, data).create_savedsearch()
        savedsearch_name = PageNewSavedsearch(self.driver, data).create_new_savedsearch()

        PageLateralRequest(self.driver, data).open_edit_savedsearchs()
        try:
            self.assertTrue(PageSavedsearch(self.driver, data).search_savedsearches(savedsearch_name))

        except AssertionError as e:
            raise Exception('Error during saved search creation', e)


if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_783, data, __main__)
