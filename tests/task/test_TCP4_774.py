#!/usr/local/bin/python3

# Check if using local environment
from os import getenv
if getenv('ENVIRONMENT') == 'local':
    import sys
    from sys import path
    path.append('../../includes')
    from __init__ import data


from test_parent import BaseTest
from util import run_test
from page_login import PageLogin
from page_menu import PageMenu
from page_tasks import PageTasks
from page_request_task import PageRequestTask


from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

# Import util file where all helper functions are located
import util
# Import all page classes
from page import *
# Import Python unittest module
import unittest


class TCP4_774(BaseTest):
    ''' Test that a task can be opened'''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Log in to server')
        self.log.append('Step 1: Load Login page////////////////')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # For use with logs
        self.assertionFailures = []

    def test_tcp4_774(self):
        '''Opens a task'''

        # Redirect to Admin Users page, wait for +User button to be clickable
        self.log.append('Step 2: go to tasks////////////////')
        PageMenu(self.driver, data).goto_tasks()

        # Wait for user edit form to load, changes the country and save
        self.log.append('Step 3: Opens a task////////////////')
        PageTasks(self.driver, data).edit_task()
        try:
            self.assertTrue(PageRequestTask(self.driver, data).request_task_is_open())

        except AssertionError as e:
            raise Exception('Error while opening a task', e)

    def tearDown(self):
        ''' Method to run after each test method. '''
        # Runs final assert check. If assertionFailures list is empty, all assertions
        # passed. If it is not empty, assertions failed.
        self.assertEqual([], self.assertionFailures)


if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_774, data, __main__)
    print(output)
