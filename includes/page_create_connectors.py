#!/usr/local/bin/python3
""" Create Data Connectors Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import util

class PageCreateConnectors:
    ''' Page object model for create data connectors page'''
    CONNECTORS_NAME_TEXT_ID = "title"
    CONNECTORS_DESCRIPTION_TEXT_ID = "description"
    AUTHENTICATION_SELECT_XPATH = "//text()[contains(.,'Select Authentication Type')]/ancestor::div[1]"
    CATEGORY_SELECT_XPATH = "//text()[contains(.,'type here to search')]/ancestor::div[1]"
    SAVE_CONNECTORS_XPATH = "//button[contains(text(),'Save')]"


    def __init__(self, driver, data):
        ''' Instantiate PageCollection object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_connectors(self):
        ''' Function to get page elements. '''
        self.name_text = self.wait.until(EC.visibility_of_element_located((By.ID, PageCreateConnectors.CONNECTORS_NAME_TEXT_ID)))
        self.description_textarea = self.wait.until(EC.visibility_of_element_located((By.ID, PageCreateConnectors.CONNECTORS_DESCRIPTION_TEXT_ID)))
        self.authentication_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateConnectors.AUTHENTICATION_SELECT_XPATH)))
        self.category_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateConnectors.CATEGORY_SELECT_XPATH)))
        self.save_connectors_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateConnectors.SAVE_CONNECTORS_XPATH)))

        # Dynamically generated values with util.py
        self.name_text_val = util.generate_text()
        self.description_textarea_val = util.generate_text()

    def select_category(self,category):
        self.category_list.click()
        input_category = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='createDataSource']/div/div/div[2]/div[4]/div/div[2]/input")))
        input_category.send_keys(category)
        input_category.send_keys(Keys.ENTER)

    def select_authentication(self, type_auth):
        self.authentication_list.click()
        input_authentication = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//label[@for='type']/following-sibling::div/div[@class='multiselect__tags']/input")))
        input_authentication.send_keys(type_auth)
        input_authentication.send_keys(Keys.ENTER)

    def fill_new_connectors(self, type_auth, category):
        ''' Function to create a new data connectors. '''
        self.paths_connectors()
        self.name_text.send_keys(self.name_text_val)
        self.description_textarea.send_keys(self.description_textarea_val)

        self.select_authentication(type_auth)
        authentication_val = self.authentication_list.text
        if(type_auth not in authentication_val):
            self.select_authentication(type_auth)

        self.select_category(category)
        category_val = self.category_list.text
        if(len(category_val) == 0):
            self.select_category(category)

        self.save_connectors_button.click()
        connectors_data = {'connectors_name': self.name_text_val, 'connectors_description': self.description_textarea_val}
        return connectors_data

