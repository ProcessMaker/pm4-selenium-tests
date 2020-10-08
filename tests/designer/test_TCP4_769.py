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
from page_processes import PageProcesses
import unittest

class TCP4_769(BaseTest):
    ''' Test to verify import a process '''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Step 1: Load Login page////////////////')
        self.driver.get(data['server_url'])
        self.driver = PageLogin(self.driver, data).login()

    def test_create_script(self):
        ''' Import process '''
        # Constants
        self.process_result_search = None  # To save webElement, if the user was found
        self.file_name = "automation_trogdor_import_process"
        self.file_extension = ".json"

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageProcesses = PageProcesses(self.driver, data)

        # STEP 2: Go to Designer.
        self.log.append('Step 2: Go to Designer')
        pageMenu.goto_designer()

        # STEP 3: Import the process .json.
        self.log.append('Step 3: Import the process .json')
        pageProcesses.import_process(self.file_name + self.file_extension)

        # STEP 5: Go to Designer.
        self.log.append('Step 5: Go to Designer')
        pageMenu.goto_designer()

        # STEP 6: Verify if the process was imported.
        self.log.append('Step 6: Verify if the process was imported')



if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_769, data, __main__)