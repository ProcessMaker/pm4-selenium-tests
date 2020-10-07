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

class TCP4_1621(BaseTest):
    ''' Test to verify that a collection was deleted '''

    def test_delete_collection(self):
        ''' Delete collection tha was created '''
        #Constants
        collection_data = {}             # To save screen data, when you create an new screen
        collection_result_search = None  # To save webElement, if the user was found

        # Pages Instance
        pageMenu        = PageMenu(self.driver, data)
        pageCollection  = PageCollection(self.driver, data)

        # STEP 1: Load login page.
        # print('Step 1: Load Login page')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to Collections.
        # print('STEP 2: Go to Collections')
        pageMenu.goto_collections()

        # STEP 3: Create a new collection.
        # print('STEP 3: Create a new collection')
        collection_data = pageCollection.create_new_collection("","")

        # STEP 4: Go to Collections.
        # print('STEP 4: Go to Collections')
        pageCollection.goto_collection_home()

        # STEP 5: Verify if the collection was created.
        # print('STEP 5: Verify if the collection was created')
        try:
            collection_result_search = pageCollection.search_collection(collection_data['collection_name'])
            self.assertTrue(collection_result_search != None)
        except AssertionError as e:
            raise Exception('Error in search_collection function', e)

        # STEP 6: Delete the collection created.
        # print('STEP 6: Delete the collection created')
        pageCollection.delete_collection(collection_result_search)

        # STEP 7: Go to Collections.
        # print('STEP 7: Go to Collections')
        pageMenu.goto_collections()

        # STEP 8: Verify if the collection was deleted.
        # print('STEP 8: Verify if the collection was deleted')
        try:
            collection_result_search = pageCollection.search_collection(collection_data['collection_name'])
            self.assertTrue(collection_result_search == None)
        except AssertionError as e:
            raise Exception('Error in delete_collection', e)

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_1621, data, __main__)