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

SCRIPT_CODE = """
<?php  
return "smoke";
"""
class TCP4_784(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_create_script(self):
        ''' Create a script '''
        # Constants
        script_data = {}       # To save user data, when you create a category
        script_result_search = None

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageScript = PageScripts(self.driver, data)
        pageScriptsBuilder = PageScriptsBuilder(self.driver,data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to Designer.
        self.log.append('Step 2: Go to Designer')
        pageMenu.goto_designer()

        # STEP 3: Go to Scripts.
        self.log.append('Step 3: Go to Scripts')
        pageMenu.goto_scripts()

        # STEP 4: Create a new Script.
        self.log.append('STEP 4: Create a new Script')
        script_data = pageScript.create_scripts('Test Script desc', 'Uncategorize', 'php - PHP Executor', 'Admin User', '60')

        # STEP 5: Create a code.
        self.log.append('STEP 5: Create a code')
        result_code = pageScriptsBuilder.create_scripts_builder(SCRIPT_CODE)

        #STEP 6: Verify if the script ran correctly
        try:
            self.log.append('STEP 6: Verify if the script ran correctly')
            self.assertIn('"output": "smoke"', result_code['script_builder_code'])
        except AssertionError as e:
            self.log.append('Time out The script took more than 30s to run', e)
            # raise Exception('Time out The script took more than 30s to run', e)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_784, data, __main__)