#!/usr/local/bin/python3
""" Page Navigation class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageNewRequest:
    ''' Page object model for Navigation Menu. '''

    START_SPECIFIC_XPATH = "(//div[text()[contains(.,'"
    REQUEST_SEARCH_CSS = "input[placeholder='Search...']"   

    def __init__(self, driver, data):
        ''' Instantiate PageMenu object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(self.driver, 30)

    def paths_new_request(self):
        ''' Function to get page elements. '''
        self.request_popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='row no-gutters']")))
        self.start_any = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='col-2 text-right']")))   

        self.request_search = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewRequest.REQUEST_SEARCH_CSS)))  

    def open_request(self, request):
        ''' Function that opens a specific request. '''
        self.paths_new_request()

        if(request == 'any'):
            self.start_any.click()

        else:
            self.request_search.send_keys(request)
            request_name = PageNewRequest.START_SPECIFIC_XPATH + request + "')]])[3]/following-sibling::div"
            self.start_specific = self.wait.until(EC.visibility_of_element_located((By.XPATH, request_name)))
            self.start_specific.click()            

        try:
            self.tasks_table = self.wait.until(EC.visibility_of_element_located((By.ID, "requestTab")))
            passed = True

        except AssertionError as e:
            passed = False
            raise Exception('Error while opening request', e)

        return passed