#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException


class PageSavedsearch:
    ''' Page object model for saved searches. '''

    SEARCH_SAVEDSEARCH_CSS = "input[placeholder= 'Search']"
    SEARCH_RESULTS_CSS = "tr[item-index= '0']"

    def __init__(self, driver, data):
        ''' Instantiate PageLogin class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_lateral_menu(self):
        ''' Function to get page elements. '''
        self.search_savedsearch = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageSavedsearch.SEARCH_SAVEDSEARCH_CSS)))

    def search_savedsearches(self, name):
        ''' Searches for the savedsearch. '''
        self.paths_lateral_menu()
        self.search_savedsearch.send_keys(name)
        try:
            self.search_savedsearch = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageSavedsearch.SEARCH_RESULTS_CSS)))
            return(True)
        except TimeoutException:
            return(False)
