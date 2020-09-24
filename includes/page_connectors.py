#!/usr/local/bin/python3
""" Data Connectors Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_create_connectors import PageCreateConnectors
import time

class PageConnectors:
    ''' Page object model for data connectors page'''
    CREATE_CONNECTORS_BUTTON_ID = "create_datasource"
    CONNECTORS_SEARCH_BAR_XPATH = "//*[@placeholder='Search']"
    CONNECTORS_TABLE_XPATH = "//*[@id='dataSourceIndex']/div[2]/div[2]"
    LOADING_MESSAGE_XPATH = "//*[@id='dataSourceIndex']/div[2]/div[1]"

    CONFIRM_DELETE_BUTTON_XPATH = "//button[text()='Confirm']"

    def __init__(self, driver, data):
        ''' Instantiate PageCollection object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_connectors(self):
        ''' Function to get page elements. '''
        self.create_connectors_button = self.wait.until(EC.visibility_of_element_located((By.ID, PageConnectors.CREATE_CONNECTORS_BUTTON_ID)))
        self.connectors_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageConnectors.CONNECTORS_SEARCH_BAR_XPATH)))

    def create_new_connectors(self, type_auth, category):
        ''' Function to create a new data connectors. '''
        self.paths_connectors()
        self.create_connectors_button.click()
        connectors_data = PageCreateConnectors(self.driver, self.data).fill_new_connectors(type_auth, category)
        return connectors_data

    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        try:
            while True:
                result_search = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, PageConnectors.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                if "Loading" not in cad and len(cad) != 0:
                    break

            msg = self.driver.find_element(By.XPATH, PageConnectors.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, PageConnectors.CONNECTORS_TABLE_XPATH).value_of_css_property("display")

            if msg == 'none' and table != 'none':
                return True
            else:
                return False
        except TimeoutException:
            return True

    def search_connectors(self, connector_name):
        ''' Search for a connector_name: return webElement if this exits and return None if the connector dont exits'''

        self.paths_connectors()
        self.connectors_search_bar.send_keys(connector_name)

        # Wait until the search ends
        connector_founded = self.search_wait_loading()

        # Iterate through the list to check if the connector with connector_name is found
        if connector_founded:
            table_connector = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageConnectors.CONNECTORS_TABLE_XPATH)))
            table_content = table_connector.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                connector = col[0].text
                if (connector == connector_name):
                    # returns the column where the edit and delete buttons are located
                    return col[5]
            return None
        else:
            return None

    def delete_connector(self, element):
        buttons = element.find_elements(By.TAG_NAME, "button")
        buttons[1].click()
        confirm_deleted_connector = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageConnectors.CONFIRM_DELETE_BUTTON_XPATH)))
        confirm_deleted_connector.click()
        delete_connector_succes = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

