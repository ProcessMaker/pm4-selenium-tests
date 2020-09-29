#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import string
import util
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PageScriptsBuilder:
    ''' Page object model for category page'''
    # constants
    SCRIPT_BUILD_BUTTON_RUN_CSS = "button[class='btn text-capitalize pl-3 pr-3 btn-secondary btn-sm']"
    SCRIPT_BUILD_OUTPUT_CSS = "div[class='output text-white']"
    SCRIPT_BUILD_SAVE_CSS = "div.p-0>button"


    FINISH_LOADING_SCRIPT_XPATH = "//i[@class='fas fa-check text-success']"
    TEXT_OUTPUT_CSS = "pre.text-white>samp"


    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 40)

    def paths_create_scripts_builder(self):
        ''' Function to get page elements. '''
        self.button_run = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_BUTTON_RUN_CSS)))
        self.button_save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_SAVE_CSS)))
        
    def create_scripts_builder(self, code):
        self.paths_create_scripts_builder()
        self.put_script_code(code)
        self.save_script_builder()
        self.run_script_builder()
        output = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TEXT_OUTPUT_CSS)))
        script_code = {
            'script_builder_code': output.text
            }
        return script_code

    def save_script_builder(self):
        self.paths_create_scripts_builder()
        self.button_save.click()
        save = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.modal-body>div.modal-footer>button.btn.btn-secondary")))
        save.click()
        save_script_succes = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def run_script_builder(self):
        self.button_run.click()
        # wait = WebDriverWait(self.driver, 30)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, PageScriptsBuilder.FINISH_LOADING_SCRIPT_XPATH)))

    def put_script_code(self, code):
        textarea =self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='script-container']/div/div/div[2]/div/div[1]/div/div/div[1]/textarea")))
        textarea.send_keys(Keys.CONTROL + "a")
        textarea.send_keys(Keys.DELETE)
        # with open("script.php") as f:
        #     script_php = f.read()
        textarea.send_keys(code)
