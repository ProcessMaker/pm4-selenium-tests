#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test, login
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test, login

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestScreenDateInput(BaseTest):
    ''' Test date input on Screens behaves as expected. '''

    def test_screen_date_input(self):
        ''' Test that user can login and the Designer page displays. '''

        # Login using configured url, workspace, username, and password
        self.driver = login(data['server_url'], data['username'], data['password'], self.driver)

        # Wait for Designer link to load
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Designer')))

        # Verify that link is clickable
        self.assertTrue(self.driver.find_element_by_link_text('Designer').is_displayed())


if __name__ == "__main__":
    import __main__
    output = run_test(TestScreenDateInput, data, __main__)