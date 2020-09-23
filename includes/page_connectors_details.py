#!/usr/local/bin/python3
""" Create Data Connectors Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import util
import sys

class PageConnectorsDetails:
    ''' Page object model for connectors details page'''
    DETAILS_LINK_ID = "__BVID__45___BV_tab_button__"
    AUTHORIZATIONS_LINK_ID = "__BVID__51___BV_tab_button__"
    ENDPOINTS_LINK_ID = "__BVID__53___BV_tab_button__"
    SAVE_AUTHORIZATIONS_XPATH = "//button[text()='Save']"

    AUTHENTICATION_LIST_XPATH = "//label[@for='auth']/following-sibling::div/div[@class='multiselect__tags']"
    AUTHENTICATION_INPUT_XPATH = "//label[@for='auth']/following-sibling::div/div[@class='multiselect__tags']/input"
    USER_TEXT_ID = "user"
    PASSWORD_TEXT_ID = "password"

    def __init__(self, driver, data):
        ''' Instantiate PageCollectionsDetails object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_connectors_details(self):
        ''' Function to get page elements. '''
        self.details_link = self.wait.until(EC.visibility_of_element_located((By.ID, PageConnectorsDetails.DETAILS_LINK_ID)))
        self.authorization_link = self.wait.until(EC.visibility_of_element_located((By.ID, PageConnectorsDetails.AUTHORIZATIONS_LINK_ID)))
        self.endpoints_link = self.wait.until(EC.visibility_of_element_located((By.ID, PageConnectorsDetails.ENDPOINTS_LINK_ID)))

    def select_method(self, type_Auth):
        method_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageConnectorsDetails.AUTHENTICATION_LIST_XPATH)))
        method_list.click()
        method_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageConnectorsDetails.AUTHENTICATION_INPUT_XPATH)))
        method_input.send_keys(type_Auth)
        method_input.send_keys(Keys.ENTER)

    def fill_authorizations(self, type_Auth,user_name, user_password):
        self.paths_connectors_details()
        self.authorization_link.click()
        self.select_method(type_Auth)
        user_text = self.wait.until(EC.visibility_of_element_located((By.ID, PageConnectorsDetails.USER_TEXT_ID)))
        password_text = self.wait.until(EC.visibility_of_element_located((By.ID, PageConnectorsDetails.PASSWORD_TEXT_ID)))
        save_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageConnectorsDetails.SAVE_AUTHORIZATIONS_XPATH)))

        user_text.send_keys(user_name)
        password_text.send_keys(user_password)
        save_button.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))



