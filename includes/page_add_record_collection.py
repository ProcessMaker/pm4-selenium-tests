#!/usr/local/bin/python3
""" Add Record Collections Page class. """

from page_create_collection import PageCreateCollection

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import util


class PageAddRecordCollection:
    ''' Page object model for add record to collections page'''
    NAME_RECORD_INPUT_XPATH = "//input[@type='text'][@name='name']"
    OPTION_RECORD_INPUT_XPATH = "//input[@type='text'][@name='option']"
    SAVE_RECORD_BUTTON_XPATH = "//button[text()='Submit']"

    def __init__(self, driver, data):
        ''' Instantiate PageCollection object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_add_record_collection(self):
        ''' Function to get page elements. '''
        self.name_record_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageAddRecordCollection.NAME_RECORD_INPUT_XPATH)))
        self.option_record_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageAddRecordCollection.OPTION_RECORD_INPUT_XPATH)))
        self.save_record_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageAddRecordCollection.SAVE_RECORD_BUTTON_XPATH)))

        # Dynamically generated values with util.py
        self.name_record_val = util.generate_text()
        self.option_record_val = '1' + util.generate_numbers(2)

    def fill_data_record(self):
        ''' Function to fill data a  record of a collection. '''
        self.paths_add_record_collection()
        self.name_record_input.send_keys(self.name_record_val)
        self.option_record_input.send_keys(self.option_record_val)
        self.save_record_button.click()

        # Returns record data of the form
        record_data = {'record_name': self.name_record_val, 'record_option': self.option_record_val}
        return record_data
