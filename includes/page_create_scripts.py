#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import string
import util
from selenium.webdriver.common.keys import Keys

class PageCreateScript:
    ''' Page object model for category page'''
    # constants    
    SCRIPT_MODAL_ID = "addScript"
    SCRIPT_NAME_ID = "title"
    SCRIPT_DESCRIPTION_ID = "description"
    SCRIPT_CATEGORY_XPATH = "//span[contains(.,'type here to search')]//parent::div//parent::div"
    SCRIPT_OPTION_CATEGORY_CSS = "li[class='multiselect__element']"
    SCRIPT_LANGUAGE_ID = "script_executor_id"
    SCRIPT_OPTION_RUN_SCRIPT_AS_CSS = "div[class='multiselect multiselect--above']"
    SCRIPT_RUN_SCRIPT_XPATH = "//span[contains(.,'Select')]//parent::div//parent::div"
    SCRIPT_TIME_OUT_CSS = "input[id='timeout']"
    SCRIPT_SAVE_BUTTON_CLASS = "btn-secondary"
    SCRIPT_CANCEL_BUTTON_CLASS = "btn-outline-secondary"


    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_create_scripts(self):
        ''' Function to get page elements. '''
        modal = self.wait.until(EC.visibility_of_element_located((By.ID, self.SCRIPT_MODAL_ID)))
        self.name = modal.find_element_by_id(self.SCRIPT_NAME_ID)
        self.description = modal.find_element_by_id(self.SCRIPT_DESCRIPTION_ID)
        self.category = modal.find_element_by_xpath(self.SCRIPT_CATEGORY_XPATH)
        self.language = Select(modal.find_element_by_id(self.SCRIPT_LANGUAGE_ID))
        self.run_script_as = modal.find_element_by_xpath(self.SCRIPT_RUN_SCRIPT_XPATH)
        self.time_out = modal.find_element_by_css_selector(self.SCRIPT_TIME_OUT_CSS)
        self.save_button = modal.find_element_by_class_name(self.SCRIPT_SAVE_BUTTON_CLASS)
        self.cancel_button = modal.find_element_by_class_name(self.SCRIPT_CANCEL_BUTTON_CLASS)

    def create_scripts(self, description, category, language, runScript, timeout):
        self.paths_create_scripts()
        name = 'script-' + util.generate_text()
        self.name.send_keys(name)
        self.description.send_keys(description)
        self.category.click()
        self.option_category = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_OPTION_CATEGORY_CSS))) 
        self.category.send_keys(category)
        self.language.select_by_visible_text(language)
        self.run_script_as.click()
        self.run_script_as.send_keys(runScript)
        option = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'"+runScript+"')]")))
        self.run_script_as.send_keys(Keys.ENTER)
        self.time_out.clear()
        self.time_out.send_keys(timeout)
        self.save_button.click()
        script_data = {
            'script_name': name,
            'script_description': description,
            'script_category': category,
            'script_language': language,
            'script_runScript': runScript,
            'script_timeOut': timeout
            }
        return script_data
