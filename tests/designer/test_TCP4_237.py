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

class TCP4_237(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_create_active_category(self):
        ''' Create an active screen category '''
        #Constants
        category_data = {}       # To save user data, when you create a category
        category_result_search = None
        
        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        PageProcess = PageProcesses(self.driver, data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to Designer.
        self.log.append('Step 2: Go to Designer')
        pageMenu.goto_designer()

        # STEP 3: Create a new Category with active status.
        self.log.append('STEP 3: Create a new category with active status.')
        category_data = PageProcess.create_category('active')
        
        try:
            # STEP 4: Verify the Category
            category_result_search = PageProcess.search_category(category_data['category_name'])
            #print(category_result_search)
            self.assertTrue(category_result_search!=None)
        except AssertionError as e:
            raise Exception('Error in search_category',e)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_237, data, __main__)