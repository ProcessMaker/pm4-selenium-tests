#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from page_create_category import PageCreateCategory
import time


class PageExportProcess:
    ''' Page object model for users page'''
    SAVE_BUTTON = "div[class = 'card-footer bg-light'] > [class = 'btn btn-secondary ml-2']"
    EXPORTED_PROCESS = "pre[style='word-wrap: break-word; white-space: pre-wrap;']"
    

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_export_processes(self):
        ''' Function to get page elements. '''
        self.save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SAVE_BUTTON)))

    def export_process(self):
        '''Function to delete a category from process'''
        self.paths_export_processes()
        self.save_button.click()
        self.driver.get("file://C://Users//zolut//Downloads//fROxxxBOLj_Process_Self_Service.json")
        try:
            self.exported_process = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.EXPORTED_PROCESS)))
            passed = True

        except AssertionError as e:
            passed = False
            raise Exception('Error while opening exported process', e)

        return passed
