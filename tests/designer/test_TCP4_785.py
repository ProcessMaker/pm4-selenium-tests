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
from page_connectors import PageConnectors
from page_connectors_details import PageConnectorsDetails
import unittest

class TCP4_785(BaseTest):
    ''' Test to verify Creates Data Connectors '''

    def test_create_data_connectors(self):
        ''' Create Data connectors '''

        # Constants
        connectors_data = {}  # To save data, when you create an connector
        connectors_result_search = None  # To save webElement, if the data connectors was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageConnectors = PageConnectors(self.driver, data)
        pageConnectorsDetails = PageConnectorsDetails(self.driver, data)

        # STEP 1: Load login page.
        # print('Step 1: Load Login page')
        self.log.append('Step 1: Load Login page////////////////')
        self.driver = PageLogin(self.driver, data).login()

        # STEP 2: Go to data connectors.
        # print('STEP 2: Go to data connectors')
        self.log.append('Step 2: Go to data connectors////////////////')
        pageMenu.goto_connectors()

        # STEP 3: Create data connectors with type_Auth = No Auth.
        # print('STEP 3: Create data connectors with type_Auth = No Auth.')
        self.log.append('Step 3: Creates a data connector with no auth////////////////')
        connectors_data = pageConnectors.create_new_connectors("No Auth","")

        # STEP 4: Fill Authorization with Fill Method: Basic Auth; user: admin; password: admin.
        # print('STEP 4: Fill Authorization with Fill Method: Basic Auth; user: admin; password: admin.')
        self.log.append('Step 4: Fills the auth with basic auth////////////////')
        pageConnectorsDetails.fill_authorizations("Basic Auth", "admin", "admin")

        # STEP 5: Go to data connectors.
        # print('STEP 5: Go to data connectors')
        self.log.append('Step 5: Go to data connectors////////////////')
        pageMenu.goto_connectors()

        # STEP 6: Verify if the data connector was created
        try:
            # print('STEP 6: Verify if the data connector was created')
            self.log.append('Step 6: Verify the data conector exists////////////////')
            connectors_result_search = pageConnectors.search_connectors(connectors_data['connectors_name'])
            self.assertTrue(connectors_result_search is not None)
            # print('Data connector was found')
        except AssertionError as e:
            raise Exception('Error in create data connector function', e)
            # print('Data connector was not created, an error ocurred')

        # print('Create User Test completed')

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_785, data, __main__)