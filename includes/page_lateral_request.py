#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageLateralRequest:
    ''' Page object model for lateral request. '''

    def __init__(self, driver, data):
        ''' Instantiate lateral request class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_lateral_menu(self):
        ''' Function to get page elements. '''

    def open_edit_savedsearchs(self):
        ''' opens the saved searches edit menu '''
        self.driver.get(self.data['server_url'] + 'requests/saved-searches')
