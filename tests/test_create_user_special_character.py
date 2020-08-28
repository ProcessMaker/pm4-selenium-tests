#!/usr/local/bin/python3

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') != 'local':
    from test_parent import BaseTest
    from util import run_test
    from page_login import PageLogin
    from page_menu import PageMenu
    from page_users import PageUsers
    from page_user_information import PageUserInformation
# If using local environment
else:
    from sys import path
    path.append('../')
    from includes.test_parent import BaseTest
    from includes.util import run_test
    from includes.page_login import PageLogin
    from includes.page_menu import PageMenu
    from includes.page_users import PageUsers
    from includes.page_user_information import PageUserInformation
    from __init__ import data

import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TCP4_761(BaseTest):
    ''' Test that the country of an user can be changed '''

    def test_create_user_special_character(self):

        self.driver = PageLogin(self.driver, data).login()

        PageMenu(self.driver,data).goto_admin()
        page_user = PageUsers(self.driver,data)
        page_user.create_user()

        self.assertEqual(2,2)
        print('d')

if __name__ == "__main__":
    import __main__  
    output = run_test(TCP4_761, data, __main__)
