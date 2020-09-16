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
import unittest

class TCP4_768(BaseTest):
    ''' Creates a process '''

    def test_tcp4_768(self):
        ''' Creates a process '''
        # constants
        process_name = None

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageProcesses = PageProcesses(self.driver, data)
        pageNewProcess = PageNewProcess(self.driver, data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: Go to the designer section.
        self.log.append('Step 2: Opens the designer section')        
        pageMenu.goto_processes()

        # STEP 3: Creates a new process.
        self.log.append('Step 3: Creates a new process')   
        pageProcesses.create_process()

        try:
            # print('Step 5: Verify if the user was created')       
            self.assertTrue(pageNewProcess.fill_new_process('any'))

        except AssertionError as e:
            self.log.append(e,' There was an error during process creation')    
        


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_768, data, __main__)


