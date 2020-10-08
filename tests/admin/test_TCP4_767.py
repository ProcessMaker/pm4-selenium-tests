#!/usr/local/bin/python3

# Check if using local environment
from os import getenv
import os.path
if getenv('ENVIRONMENT') == 'local':
    import sys
    from sys import path

    path.append('../../includes')
    from __init__ import data

from test_parent import BaseTest
import util
import unittest
from page_login import PageLogin
from page_menu import PageMenu
from page_collections import PageCollection

class TCP4_767(BaseTest):
    ''' Test to verify import a collections'''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Step 1: Load Login page////////////////')
        self.driver.get(data['server_url'])
        self.driver = PageLogin(self.driver, data).login()

    def test_import_collection(self):

        # Constants
        self.collection_result_search = None  # To save webElement, if the user was found
        self.file_name = "automation_trogdor_import_collection"
        self.file_extension = ".json"

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageCollection = PageCollection(self.driver, data)

        self.log.append('Step 2: Go to Collection')
        pageMenu.goto_collections()

        self.log.append('Step 3: Import file to collection')
        pageCollection.import_collection(self.file_name + self.file_extension)

        self.log.append('Step 2: Go to Collection')
        pageMenu.goto_collections()

        # STEP 5: Verify if the collection was created.
        self.log.append('Step 4: Import file to collection')
        try:
            self.collection_result_search = pageCollection.search_collection(self.file_name)
            self.assertTrue(self.collection_result_search is not None)
        except AssertionError as e:
            self.log.append('Error in search_collection function////////////////')
            raise Exception('Error in search_collection function', e)

        self.log.append('Test created collection completed////////////////')


    def tearDown(self):
        ''' Method to run after each test method. '''
        # STEP 5: Delete uploaded file.
        self.log.append('Step 5: Delete uploaded file')
        PageCollection(self.driver, data).delete_collection(self.collection_result_search)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_767, data, __main__)