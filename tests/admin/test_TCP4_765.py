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
from page_collections import PageCollection
import unittest


class TCP4_765(BaseTest):
    ''' Test to verify that a collection was created '''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Step 1: Load Login page////////////////')
        self.driver.get(data['server_url'])
        self.driver = PageLogin(self.driver, data).login()

    def test_create_collection(self):
        ''' Create user with Complete User information '''
        # Constants
        self.collection_data = {}             # To save screen data, when you create an new screen
        self.collection_result_search = None  # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageCollection = PageCollection(self.driver, data)

        # STEP 2: Go to Collections.
        # print('STEP 2: Go to Collections')
        self.log.append('Step 2: Go to collections////////////////')
        pageMenu.goto_collections()

        # STEP 3: Create a new collection.
        # print('STEP 3: Create a new collection')
        self.log.append('Step 3: Create a collection////////////////')
        self.collection_data = pageCollection.create_new_collection("", "")

        # STEP 4: Go to Collections.
        # print('STEP 4: Go to Collections')
        self.log.append('Step 4: Go to collections////////////////')
        pageCollection.goto_collection_home()

        # STEP 5: Verify if the collection was created.
        # print('STEP 5: Verify if the collection was created')
        self.log.append('Step 5: Verify created collection////////////////')
        try:
            self.collection_result_search = pageCollection.search_collection(self.collection_data['collection_name'])
            self.assertTrue(self.collection_result_search is not None)
        except AssertionError as e:
            self.log.append('Error in search_collection function////////////////')
            raise Exception('Error in search_collection function', e)

        self.log.append('Test created collection completed////////////////')

    def tearDown(self):
        ''' Method to run after each test method. '''
        # STEP 6: Deleted user created.
        self.log.append('Step 6: Delete Collection////////////////')
        PageCollection(self.driver, data).delete_collection(self.collection_result_search)

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_765, data, __main__)

