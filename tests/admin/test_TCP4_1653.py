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

class TCP4_1653(BaseTest):
    ''' Test to verify PMQL query'''

    def test_search_pmql_query(self):
        ''' Put a PMQL query in searcher a collection '''
        # Constants
        record_collection_data = {}  # To save record data, when you create a new record
        collection_result_search = None  # To save webElement, if the collection was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageCollection = PageCollection(self.driver, data)
        pageRecordCollection = PageRecordCollection(self.driver, data)

        # STEP 1: Load login page.
        # print('Step 1: Load Login page')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to Collections.
        # print('STEP 2: Go to Collections')
        pageMenu.goto_collections()

        # STEP 3: Search the collection to add Records.
        # print('STEP 3: Search the collection to add Records')
        try:
            collection_result_search = pageCollection.search_collection('AutomationTrogdorCollection001')
            self.assertTrue(collection_result_search is not None)
        except AssertionError as e:
            raise Exception('Error in search_collection function', e)

        # STEP 4: Select the collection.
        # print('STEP 4: Select the collection')
        pageCollection.select_collection(collection_result_search)

        # STEP 5: Open record form.
        # print('STEP 5: Open record form')
        record_collection_data = pageRecordCollection.add_record()

        # STEP 6: Verify PMQL query using Equal to.
        # print('STEP 6: Verify PMQL query using Equal to')
        try:
            result_record = pageRecordCollection.search_record_pmql_equal(record_collection_data['record_option'])
            self.assertTrue(result_record)
        except AssertionError as e:
            raise Exception('Error in search with Equal to', e)

        pageRecordCollection.clean_search_box()

        # STEP 7: Verify PMQL query using Less than or equal to.
        # print('STEP 7: Verify PMQL query using Less than or equal to.')
        try:
            result_record = pageRecordCollection.search_record_pmql_less_than_or_equal_to(record_collection_data['record_option'])
            self.assertTrue(result_record)
        except AssertionError as e:
            raise Exception('Error in search with Less than or equal to', e)

        pageRecordCollection.clean_search_box()

        # STEP 8: Verify PMQL query using greater than or equal to.
        # print('STEP 8: Verify PMQL query using greater than or equal to.')
        try:
            result_record = pageRecordCollection.search_record_pmql_greater_than_or_equal_to(record_collection_data['record_option'])
            self.assertTrue(result_record)
        except AssertionError as e:
            raise Exception('Error in search with greater than or equal to', e)

        pageRecordCollection.clean_search_box()

        # STEP 9: Verify PMQL query using AND.
        # print('STEP 9: Verify PMQL query using AND')
        try:
            result_record = pageRecordCollection.search_record_pmql_and(record_collection_data['record_option'])
            self.assertTrue(result_record)
        except AssertionError as e:
            raise Exception('Error in search with AND', e)

        pageRecordCollection.clean_search_box()

        # print('Completed test search pmql query')

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_1653, data, __main__)
