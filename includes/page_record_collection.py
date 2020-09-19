#!/usr/local/bin/python3
""" Add Record Collections Page class. """

from page_add_record_collection import PageAddRecordCollection

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import util


class PageRecordCollection:
    ''' Page object model for record to collections page'''
    ADD_RECORD_BUTTON_ID = "addUserCollection"
    SEARCH_COLLECTION_BAR_XPATH = "//input[@type='text'][@placeholder='PMQL']"
    LOADING_MESSAGE_XPATH = "//*[@id='recordIndex']/div[2]/div/div[1]"
    RECORDS_TABLE_XPATH = "//*[@id='recordIndex']/div[2]/div/div[2]"
    SEARCH_BUTTON_XPATH = "//button[@class='btn btn-search-run btn-primary']"

    def __init__(self, driver, data):
        ''' Instantiate PageCollection object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_record_collection(self):
        """ Function to get page elements. """
        self.add_record_button = self.wait.until(
            EC.visibility_of_element_located((By.ID, PageRecordCollection.ADD_RECORD_BUTTON_ID)))
        self.search_collection_bar = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageRecordCollection.SEARCH_COLLECTION_BAR_XPATH)))
        self.search_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageRecordCollection.SEARCH_BUTTON_XPATH)))

    def add_record(self):
        ''' Function to add a record to collection. '''
        self.paths_record_collection()
        self.add_record_button.click()
        record_data = PageAddRecordCollection(self.driver, self.data).fill_data_record()
        self.wait.until(EC.visibility_of_element_located((By.ID, PageRecordCollection.ADD_RECORD_BUTTON_ID)))
        return record_data

    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, PageRecordCollection.LOADING_MESSAGE_XPATH)))

        record_table = self.driver.find_element(By.XPATH, PageRecordCollection.RECORDS_TABLE_XPATH)
        table_content = record_table.find_element(By.TAG_NAME, 'tbody')
        rows = table_content.find_elements(By.TAG_NAME, 'tr')
        if "No Data Available" in record_table.text and len(rows) == 1:
            return False
        else:
            return True

    def search_record(self, name):
        ''' Function to get a record in the list. '''
        criteria = 'data.option' + name
        self.paths_record_collection()
        self.search_collection_bar.send_keys(criteria)

        self.search_button.click()
        return self.search_wait_loading()

    def search_record_pmql_equal(self, value):
        ''' Function to search a record in the list using =. '''
        return self.search_record('=' + value)

    def clean_search_box(self):
        ''' Function to clear of text box '''
        self.search_collection_bar.clear()