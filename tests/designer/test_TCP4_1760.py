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
from page_screens import PageScreens
import unittest

class TCP4_1760(BaseTest):
    ''' Test to verify if a screen was imported'''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # STEP 1: Load Login page.
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        self.driver = PageLogin(self.driver, data).login()

    def test_import_screen(self):
        ''' Import Screen '''

        # Constants
        self.screen_result_search = None  # To save webElement, if the screen was found
        self.file_name = "automation_trogdor_import_screen"
        self.file_extension = ".json"

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageScreens = PageScreens(self.driver, data)

        # STEP 2: Go to Screen Page.
        self.log.append('Step 2: Go to Screen Page')
        pageMenu.goto_designer_screen()

        # STEP 3: Import screen on designer.
        self.log.append('Step 3: Import screen on designer')
        pageScreens.import_screen(self.file_name + self.file_extension)

        # STEP 4: Go to Screen Page.
        self.log.append('Step 4: Go to Screen Page')
        pageMenu.goto_designer_screen()

        # STEP 5: Verify if the screen was imported.
        self.log.append('Step 5: Verify if the screen was imported')
        try:
            self.screen_result_search = pageScreens.search_screen(self.file_name)
            self.assertTrue(self.screen_result_search is not None)
        except AssertionError as e:
            self.log.append('Error in search_screen function')
            raise Exception('Error in search_screen function', e)

        self.log.append('Test import screen completed')

    def tearDown(self):
        ''' Method to run after each test method. '''
        # STEP 6: Delete uploaded file.
        self.log.append('Step 6: Delete uploaded file')
        PageScreens(self.driver, data).delete_screen(self.screen_result_search)

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_1760, data, __main__)
    print(output)