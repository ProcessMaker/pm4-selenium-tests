#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from page_create_category import PageCreateCategory

from util import generate_text


class PageNewScreen:
    ''' Page object model for users page'''
    NAME_ID = "title"
    TYPE_ID = "type"
    FORM_TYPE_CSS = "option[value='FORM']"
    DESCRIPTION_ID = "description"
    CATEGORY_CSS = "span[class='multiselect__placeholder']"
    CATEGORY_ANY_CSS = "li[class='multiselect__element']"

    SAVE_CSS = "button[class='btn btn-secondary']"

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_new_screens(self):
        ''' Function to get page elements. '''
        self.name = self.wait.until(EC.visibility_of_element_located((By.ID, PageNewScreen.NAME_ID)))
        self.type = self.wait.until(EC.visibility_of_element_located((By.ID, PageNewScreen.TYPE_ID)))
        self.form_type = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewScreen.FORM_TYPE_CSS)))
        self.description = self.wait.until(EC.visibility_of_element_located((By.ID, PageNewScreen.DESCRIPTION_ID)))
        self.category = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewScreen.CATEGORY_CSS)))

        self.save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewScreen.SAVE_CSS)))

    # tab and buttons
    def fill_screen(self):
        ''' Function to click tab processecs. '''
        self.paths_new_screens()
        name = generate_text()

        self.name.send_keys(name)
        self.type.click()
        self.form_type.click()
        self.description.send_keys("screen created by trogdor")
        self.category.click()
        self.category_any = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.CATEGORY_ANY_CSS)))
        self.category_any.click()

        self.save.click()
