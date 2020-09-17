#!/usr/local/bin/python3
""" Users Page class. """

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

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageRequestTask:
    ''' Page object model for users page'''

    def __init__(self, driver, data):
        ''' Instantiate PageRequestTask object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_request_tasks(self):
        ''' Function to get page elements. '''
        self.request_form = self.wait.until(EC.visibility_of_element_located((By.ID, "pending-tab")))

    def request_task_is_open(self):
        ''' Confirm the task request is open. '''
        self.paths_request_tasks()
        return (self.request_form.is_enabled())
