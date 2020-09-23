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
from page_processes import PageProcesses
from page_new_process import PageNewProcess
from page_process_canvas import PageProcessCanvas
import unittest
import time


class TCP4_775(BaseTest):
    ''' Creates a process '''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'])

        # Log in and note step in log
        self.log.append('Log in to server')
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # For use with logs
        self.assertionFailures = []

    def test_tcp4_775(self):
        ''' Creates a process '''
        # constant
        process_category = "any"

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageProcesses = PageProcesses(self.driver, data)
        pageNewProcess = PageNewProcess(self.driver, data)
        pageProcessCanvass = PageProcessCanvas(self.driver, data)

        # STEP 2: Go to the designer section.
        self.log.append('Step 2: Opens the designer section')
        pageMenu.goto_designer()

        # STEP 3: Creates a new process.
        self.log.append('Step 3: Creates a new process')
        pageProcesses.create_process()
        pageNewProcess.fill_new_process(process_category)

        # STEP 4: Fills process.
        self.log.append('Step 4: Fills a process')

        # Drages every element by an offset of X, Y
        pageProcessCanvass.drag_n_drop("start_origin", 300, 100)
        pageProcessCanvass.drag_n_drop("task_origin", 300, 100)
        pageProcessCanvass.drag_n_drop("end_origin", 300, 300)

        # Connects two previously dragged elements
        pageProcessCanvass.connect_element("start", "task")
        pageProcessCanvass.connect_element("task", "end")

        # Assert the saving was succesfull
        try:
            self.assertTrue(pageProcessCanvass.save_process())
        except AssertionError as e:
            raise Exception('Error in search_collection function', e)

    def tearDown(self):
        ''' Method to run after each test method. '''
        # Runs final assert check. If assertionFailures list is empty, all assertions
        # passed. If it is not empty, assertions failed.
        self.assertEqual([], self.assertionFailures)


''' Main call. Only used in test file.
'''
if __name__ == "__main__":

    ''' Import __main__ to use as parameter for method calls.
    '''
    import __main__

    ''' Assign to data as a key, val pair in order to append relative paths and import files.
    repository_path and data are found in the bootstrap.py file for the Docker container.
    Must be referenced in __main__ call and then passed elsewhere. May be edited elsewhere.
    data['repository_path'] = repository_path
    '''

    ''' You may add any key, value pairs to the data object.
    data comes with:
      data['server_url']
      data['username']
      data['password']
    '''

    ''' output is given back to bootstrap.py after the test is run.
    It is a dictionary with "result" and "message" key, value pairs.
    run_test() is the method that provides this dictionary. It requires the class name,
      the data object, and the __main__ module.
    '''
    output = util.run_test(TCP4_775, data, __main__)
