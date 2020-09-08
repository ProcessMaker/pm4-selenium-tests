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


class TCP4_870(BaseTest):
    ''' Verify the login for an active user '''

    def test_tcp4_870(self):
        # Login using configured url, workspace, username, and password as Administrator user
        self.driver = PageLogin(self.driver, data).login()

        # Redirect to Admin Users page
        PageMenu(self.driver, data).goto_admin()
        
        # Validate if the user exists and obtain a user and password
        user = PageUsers(self.driver, data).verifyUser()
        
        # Logout as Administrator user
        PageMenu(self.driver, data).log_out()

        # Login using configured url, workspace, username, and password as an Inactive user
        self.driver = PageLogin(self.driver, data).loginNoAdmin(user[0],user[1])

        # The inactive user does not access
        self.assertEqual(self.driver.current_url,data['server_url'] + '/requests')

if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_870, data, __main__)
    print(output)