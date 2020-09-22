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
from page_screens import PageScreens
from page_screen_designer import PageScreenDesigner

import unittest
import time


class TCP4_770(BaseTest):
    ''' Test to verify create a screen '''

    def test_create_screen_form(self):
        ''' Creates script with Form type '''
        # constants
        collection_result_search = None   # To save webElement, if the screen was found

        # Pages Instance
        pageMenu = PageMenu(self.driver, data)
        pageScreens = PageScreens(self.driver, data)
        pageScreenDesigner = PageScreenDesigner(self.driver, data)

        self.driver = PageLogin(self.driver, data).login()
        self.driver.get('https://release-testing.processmaker.net/designer/screen-builder/471/edit')

        time.sleep(5)
        pageScreenDesigner.drag_drop()
        pageScreenDesigner.location_element()
        pageScreenDesigner.save_versions()
        # pageScreenDesigner.drag_and_drop_input()

        # pageScreenDesigner.click_and_hold_1()
        # pageScreenDesigner.location_element()


if __name__ == "__main__":
    import __main__
    output = util.run_test(TCP4_770, data, __main__)
    print(output, file=sys.stderr)
