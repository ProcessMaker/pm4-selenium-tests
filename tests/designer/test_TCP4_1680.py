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


class TCP4_1680(BaseTest):
    ''' Test to verify if the a category was deleted '''

    def test_delete_category(self):
        ''' Create an active category and deleted this'''
        # Constants
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
            self.log.append('Step 4: Verigy the category////////////////')
            category_result_search = PageProcess.search_category(category_data['category_name'])
            # print(category_result_search)
            self.assertTrue(category_result_search is not None)
        except AssertionError as e:
            raise Exception('Error in search_category', e)

        # STEP 5: Deleted the category
        self.log.append('STEP 5: Deleted the category////////////////')
        PageProcess.delete_category(category_result_search)

        # STEP 6: Go to Designer.
        self.log.append('Step 6: Go to Designer')
        pageMenu.goto_designer()
        PageProcess.tab_categories()

        try:
            # STEP 7: Verify if the category was deleted
            self.log.append('STEP 7: Verify if the category was deleted////////////////')
            category_result_search = PageProcess.search_category(category_data['category_name'])
            # print(category_result_search)
            self.assertTrue(category_result_search is None)
        except AssertionError as e:
            raise Exception('Error in search_category', e)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_1680, data, __main__)