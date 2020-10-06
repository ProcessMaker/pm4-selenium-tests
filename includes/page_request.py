#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageRequest:
    ''' Page object model for request Page. '''

    NEW_SAVEDSEARCH_XPATH = "//button[@title='Save Search']"
    REQUEST_SEARCH_CSS = "input[placeholder='Process']"
    SPECIFIC_NAME_XPATH = "//td[text()='"


    def __init__(self, driver, data):
        ''' Instantiate Request class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_request(self):
        ''' Function to get page elements. '''
        self.new_savedsearch = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageRequest.NEW_SAVEDSEARCH_XPATH)))

    def create_savedsearch(self):
        ''' Creates a new saved search. '''
        self.paths_request()
        self.new_savedsearch.click()

    def search_request(self, name):
        ''' Creates a new saved search. '''
        self.paths_request()
        self.driver.executeScript ("document.getElementById ('" + PageRequest.REQUEST_SEARCH_CSS + "') .innerHTML= 'absolute'");



        request_name = PageRequest.SPECIFIC_NAME_XPATH + name + "']"
        self.start_request = self.wait.until(EC.visibility_of_element_located((By.XPATH, request_name)))
        self.start_request.click()  
