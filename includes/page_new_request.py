#!/usr/local/bin/python3
""" Page Navigation class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageNewRequest:
    ''' Page object model for Navigation Menu. '''

    def __init__(self, driver, data):
        ''' Instantiate PageMenu object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(self.driver, 30)

    def paths_new_request(self):
        ''' Function to get page elements. '''
        self.request_popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='row no-gutters']")))
        self.start_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='col-2 text-right']")))

    def open_request(self,request):
        ''' Function that opens a specific request. '''
        self.paths_new_request()

        if(request=='any'):
            self.start_button.click()
            self.tasks_table = self.wait.until(EC.visibility_of_element_located((By.ID, "requestTab")))
            return (self.tasks_table.is_enabled())