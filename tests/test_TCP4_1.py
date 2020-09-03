#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../includes')
    # Import __init__ to include data configuration
    from __init__ import data
# Import BaseTest class where webdriver instance is created
from test_parent import BaseTest
# Import util file where all helper functions are located
import util
# Import all page classes
from page import *
# Import Python unittest module
import unittest

from page_login import PageLogin
from page_users import PageUsers
from page_menu import PageMenu


class TCP4_1(BaseTest):
    ''' a string of 60 scharacters can be used in the user search input '''

    def test_tcp4_1(self):
        '''Go to the users page and input a 60 characters string in the searchbar'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Go to the admin tab
        PageMenu(self.driver, data).goto_admin()

        # Insert the 60 characters string on the searchbar
        self.assertTrue(PageUsers(self.driver, data).search_long_string())


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_1, data, __main__)
