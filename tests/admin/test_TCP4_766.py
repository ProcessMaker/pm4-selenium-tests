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
from page_record_collection import PageRecordCollection
import unittest


class TCP4_766(BaseTest):
    ''' Test to verify add record to collections'''

    def test_add_record_collection(self):
        ''' Add record in a Collection with random values '''
        # Constants
        record_collection_data = {}  # To save record data, when you create an new record
        collection_result_search = None  # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageCollection = PageCollection(self.driver, data)
        pageRecordCollection = PageRecordCollection(self.driver, data)

        # STEP 1: Load login page.
        # print('Step 1: Load Login page')
        self.log.append('Step 1: Load Login page////////////////')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to Collections.
        # print('STEP 2: Go to Collections')
        self.log.append('Step 2: Go to collections////////////////')
        pageMenu.goto_collections()

        # STEP 3: Search the collection to add Records.
        # print('STEP 3: Search the collection to add Records')
        self.log.append('Step 3: Search the collection////////////////')
        try:
            collection_result_search = pageCollection.search_collection('AutomationTrogdorCollection001')
            self.assertTrue(collection_result_search is not None)
        except AssertionError as e:
            raise Exception('Error in search_collection function', e)

        # STEP 4: Select the collection.
        # print('STEP 4: Select the collection')
        self.log.append('Step 4: Select collection////////////////')
        pageCollection.select_collection(collection_result_search)

        # STEP 5: Open record form.
        # print('STEP 5: Open record form')
        self.log.append('Step 5: Opens record form////////////////')
        record_collection_data = pageRecordCollection.add_record()

        # STEP 6: Verify if the record was created .
        # print('STEP 6: Verify if the record was created ')
        self.log.append('Step 6: Verify created record////////////////')
        try:
            result_record = pageRecordCollection.search_record_pmql_equal(record_collection_data['record_option'])
            self.assertTrue(result_record)
        except AssertionError as e:
            raise Exception('Error in add_record to collection', e)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_766, data, __main__)
