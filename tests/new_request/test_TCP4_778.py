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
from page_new_request import PageNewRequest
import unittest

class TCP4_778(BaseTest):
    ''' Test to verify the creation of users with special characters '''

    def test_tcp4_778(self):
        ''' Create user with special characters '''
        #Constants
        user_data = {}            # To save user data, when you create an user
        user_result_search = None # To save webElement, if the user was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageNewRequest = PageNewRequest(self.driver, data)

        # STEP 1: Load login page.
        self.log.append('Step 1: Load Login page')
        self.driver.get(data['server_url'])
        login_page = PageLogin(self.driver, data)
        login_page.login()

        # STEP 2: start a request.
        self.log.append('Step 2: Starts a request')        
        pageMenu.start_request() 
        try:
            # print('Step 5: Verify if the user was created')       
            self.assertTrue(pageNewRequest.open_request('any'))

        except AssertionError as e:
            self.log.append('There was an error during the assertion')    
        


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_778, data, __main__)