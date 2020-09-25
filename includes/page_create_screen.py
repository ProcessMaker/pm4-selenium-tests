#!/usr/local/bin/python3
""" Create Screen Page class. """

import util
import time
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class PageCreateScreen:
    ''' Page object model for create screens page'''
    TITLE_TEXT_ID = "title"
    TYPE_LIST_ID = "type"
    DESCRIPTION_TEXTAREA_ID = "description"
    CATEGORY_LIST_XPATH = "//text()[contains(.,'type here to search')]/ancestor::div[1]"
    SAVE_SCREEN_BUTTON_XPATH = "//button[contains(text(),'Save')]"
    CANCEL_SCREEN_BUTTON_XPATH = "//button[contains(text(),'Cancel')]"
    BASE_FORM_OPTION = "//text()[.='Base Forms']/ancestor::span[1]"

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_create_screen(self):
        ''' Function to get screen elements. '''
        self.title_text = self.wait.until(EC.visibility_of_element_located((By.ID, PageCreateScreen.TITLE_TEXT_ID)))
        self.type_list = self.wait.until(EC.visibility_of_element_located((By.ID, PageCreateScreen.TYPE_LIST_ID)))
        self.description_textarea = self.wait.until(
            EC.visibility_of_element_located((By.ID, PageCreateScreen.DESCRIPTION_TEXTAREA_ID)))
        self.category_list = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageCreateScreen.CATEGORY_LIST_XPATH)))
        self.create_screen_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageCreateScreen.SAVE_SCREEN_BUTTON_XPATH)))

        # Dynamically generated values with util.py
        self.title_val = util.generate_text()
        self.description_val = util.generate_text()
        self.category_val = 'base_form'

    def fill_new_screen_option(self, form_type):
        ''' Fills the fields of a new screen'''
        self.paths_create_screen()
        self.title_text.send_keys(self.title_val)

        for option in self.type_list.find_elements_by_tag_name('option'):
            if option.text == form_type:
                option.click()
                break
        self.description_textarea.send_keys(self.description_val)
        self.category_list.click()
        self.base_form = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageCreateScreen.BASE_FORM_OPTION)))
        self.base_form.click()
        self.create_screen_button.click()

        # Returns screen data generated
        screen_data = {'screen_title': self.title_val, 'screen_type': form_type,
                       'screen_description': self.description_val, 'screen_category': self.category_val}
        return screen_data

    def fill_new_screen_form(self):
        return self.fill_new_screen_option('Form')

    def fill_new_screen_display(self):
        return self.fill_new_screen_option('Display')

    def fill_new_screen_email(self):
        return self.fill_new_screen_option('Email')
