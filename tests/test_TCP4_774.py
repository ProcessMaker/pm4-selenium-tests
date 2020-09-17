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


class TCP4_774(BaseTest):
    ''' Test that a task can be opened'''

    def test_tcp4_774(self):
        '''Opens a task'''

        # Login using configured url, workspace, username, and password
        self.driver = PageLogin(self.driver, data).login()

        # Redirect to Admin Users page, wait for +User button to be clickable
        PageMenu(self.driver, data).goto_tasks()

        # Wait for user edit form to load, changes the country and save
        PageTasks(self.driver, data).edit_task()
        try:
            self.assertTrue(PageRequestTask(self.driver, data).request_task_is_open())

        except AssertionError as e:
            raise Exception('Error while opening a task', e)


if __name__ == "__main__":
    import __main__
    output = run_test(TCP4_774, data, __main__)
