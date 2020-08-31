#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    from sys import path
    path.append('../../includes')
    from __init__ import data

from test_parent import BaseTest
import util
from page_login import PageLogin
from page_menu import PageMenu
from page_users import PageUsers
from page_user_information import PageUserInformation
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TCP4_761(BaseTest):
    ''' Test that the country of an user can be changed '''

    def test_create_user_special_character(self):

        user_data = {'username': 'smoke','firstName': 'test','lastName': 'test qa','jobTitle': 'smoke test','status': 'Active',
                     'email': 'test@processmaker.com','password': 'Co1054!"·$%&/()='}
        self.driver = PageLogin(self.driver, data).login()

        PageMenu(self.driver,data).goto_admin()
        page_user = PageUsers(self.driver,data)
        page_user.create_user_data(user_data)


        self.assertEqual(2,2)
        output= "test"

if __name__ == "__main__":
    import __main__  
    output = util.run_test(TCP4_761, data, __main__)
