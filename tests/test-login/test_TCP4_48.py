#!/usr/local/bin/python3
""" Class to test the login page username field.
"""

# Check if using local environment
from os import getenv, path
if getenv('ENVIRONMENT') == 'local':
    from __init__ import data
    from sys import path
    path.append('../includes')

import random
import string
from test_parent import BaseTest
import util
from page import *
import unittest
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPageUsernameField(BaseTest):
    ''' Navigate to the login page and enter text into the username field. '''

    def setUp(self):
        # Load server url
        self.driver.get(data['server_url'])

    def test_that_login_username_field_accepts_long_strings(self):
        ''' Verify that a string 61+ characters long will be accepted in the username field.'''
        # Load login page.
        login_page = LoginPage(self.driver, data)

        # Check if browser is at login page
        assert login_page.is_url_matches()

        # Enter long string in username field
        long_username = util.generate_long_text()
        login_page.username_field_element = long_username

        self.assertEqual(login_page.username_field_element, long_username)


if __name__ == "__main__":
    import __main__
    output = util.run_test(TestLoginPageUsernameField, data, __main__)
