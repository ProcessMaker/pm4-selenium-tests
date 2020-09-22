#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import string
import util

class PageScriptsBuilder:
    ''' Page object model for category page'''
    # constants    
    SCRIPT_BUILD_CODE_CSS = "div[class='view-lines'"
    SCRIPT_BUILD_BUTTON_RUN_CSS = "button[class='btn text-capitalize pl-3 pr-3 btn-secondary btn-sm']"
    SCRIPT_BUILD_OUTPUT_CSS = "div[class='output text-white']"

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_create_scripts_builder(self):
        ''' Function to get page elements. '''
        self.code = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_CODE_CSS)))
        self.button_run = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_BUTTON_RUN_CSS)))
        self.output = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_OUTPUT_CSS)))
        

    def create_scripts_builder(self, code):
        self.paths_create_scripts_builder()
        self.code.send_keys(code)
        script_code = {
            'script_builder_code': code
            }
        return script_code
