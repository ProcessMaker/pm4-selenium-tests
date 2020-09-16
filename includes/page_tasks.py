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


class PageTasks:
    ''' Page object model for tasks page'''

    TASK_LIST_XPATH = "//div[@class='data-table']"
    TASK_EDIT_BUTTON_CSS = "a[class='btn btn-link']"

    def __init__(self, driver, data):
        ''' Instantiate PageTasks object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_tasks(self):
        ''' Function to get page elements. '''
        self.task_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageTasks.TASK_LIST_XPATH)))
        self.task_edit_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageTasks.TASK_EDIT_BUTTON_CSS)))

    def edit_task(self):
        ''' Function to edit a task. '''
        self.paths_tasks()
        self.task_edit_button.click()