#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from page_create_category import PageCreateCategory
import time
import os


class PageExportProcess:
    ''' Page object model for users page'''
    SAVE_BUTTON = "div[class = 'card-footer bg-light'] > [class = 'btn btn-secondary ml-2']"
    EXPORTED_PROCESS = "pre[style='word-wrap: break-word; white-space: pre-wrap;']"
    SUCCESS = "div[class='alert d-none d-lg-block alertBox alert-dismissible alert-success']"
    EXPORT_XPATH = "//td[text()='"
    

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_export_processes(self):
        ''' Function to get page elements. '''
        self.save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SAVE_BUTTON)))

    def export_process(self, process_name):
        '''Function to delete a category from process'''
        self.paths_export_processes()
        self.save_button.click()
        self.success = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SUCCESS)))
        # waits for all the files to be completed and returns the paths
        self.wait_for_downloads()
        self.driver.get("/opt/executor/~/Downloads"+process_name+".json")
        try:
            self.exported_process = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.EXPORTED_PROCESS)))
            passed = True
        except AssertionError as e:
            passed = False
            raise Exception('Error while opening exported process', e)
        return passed

    def wait_for_downloads(self):
        count = 0
        wait_download = True
        while (any([filename.endswith(".crdownload") for filename in 
                os.listdir("/opt/executor~/Downloads")])) and (wait_download):
            time.sleep(1)
            count = count + 1
            if (count >= 10):
                wait_download = False
        time.sleep(1)