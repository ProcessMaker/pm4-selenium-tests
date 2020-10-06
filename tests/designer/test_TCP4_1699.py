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
from page_scripts import PageScripts
from page_scripts_builder import PageScriptsBuilder
import unittest

class TCP4_1699(BaseTest):
    ''' Test to verify if the script was deleted'''

    def test_create_script(self):
        ''' Create and delete a script '''
        # Constants
        script_data = {}       # To save user data, when you create a category
        script_result_search = None

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageProcess = PageProcesses(self.driver, data)
        pageScripts = PageScripts(self.driver, data)
        pageScriptsBuilder = PageScriptsBuilder(self.driver,data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to Designer.
        self.log.append('Step 2: Go to Designer')
        pageMenu.goto_designer()

        # STEP 3: Go to Scripts.
        self.log.append('Step 3: Go to Scripts')
        pageMenu.goto_scripts()

        # STEP 4: Create a new Script.
        self.log.append('STEP 4: Create a new Script')
        script_data = pageScripts.create_scripts('Test Script desc', 'Uncategorize', 'php - PHP Executor', 'Admin User', '60')

        # STEP 5: Go to Scripts.
        self.log.append('Step 5: Go to Scripts')
        pageMenu.goto_scripts()

        # STEP 6: Search the Script created.
        self.log.append('STEP 6: Search the Script created')
        script_result_search = pageScripts.search_script(script_data['script_name'])

        # STEP 7: Delete the Script created.
        self.log.append('STEP 7: Delete the Script created')
        pageScripts.delete_script(script_result_search)

        # STEP 8: Go to Scripts.
        self.log.append('Step 8: Go to Scripts')
        pageMenu.goto_scripts()

        # STEP 9: Verify if the script was deleted.
        try:
            self.log.append('STEP 9: Verify if the script was deleted')
            script_result_search = pageScripts.search_script(script_data['script_name'])
            self.assertTrue(script_result_search is None)
        except AssertionError as e:
            self.log.append('Error in delete script function', e)
            raise Exception('Error in delete script function', e)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_1699, data, __main__)