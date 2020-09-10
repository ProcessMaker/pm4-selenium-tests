#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageRequest:
    ''' Page object model for Login Page. '''

    NEW_SAVEDSEARCH_CSS = "button[title='Save Search']"

    def __init__(self, driver, data):
        ''' Instantiate PageLogin class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_request(self):
        ''' Function to get page elements. '''
        self.new_savedsearch = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageRequest.NEW_SAVEDSEARCH_CSS)))

    def create_savedsearch(self):
        ''' Function to navigate to Login page. '''
        self.paths_request()
        self.new_savedsearch.click()
