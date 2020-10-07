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
        # file_name = '../../includes/file/automation_trogdor_collection001.json'
        # print(os.path.abspath(file_name), file=sys.stderr)
        # self.log.append(os.path.abspath(file_name))

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageCollection = PageCollection(self.driver, data)

        pageMenu.goto_collections()

        route =  pageCollection.import_collection(path)
        self.log.append("File includes")
        self.log.append(route)




if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_767, data, __main__)
