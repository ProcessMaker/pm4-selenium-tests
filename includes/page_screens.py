#!/usr/local/bin/python3
""" Screens Page class. """

from page_create_screen import PageCreateScreen

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys


class PageScreens:
    ''' Page object model for screens page'''
    CREATE_SCREEN_BUTTON_ID = "create_screen"
    SCREEN_SEARCH_BAR_XPATH = "//*[@placeholder='Search']"
    LOADING_MESSAGE_XPATH = "//*[@id='screenIndex']/div[2]/div[1]"
    SCREEN_TABLE_XPATH = "//*[@id='screenIndex']/div[2]/div[2]"

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_screens(self):
        ''' Function to get screen elements. '''
        self.screen_search_bar = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, PageScreens.SCREEN_SEARCH_BAR_XPATH)))
        self.create_screen_button = self.wait.until(
            EC.visibility_of_element_located((By.ID, PageScreens.CREATE_SCREEN_BUTTON_ID)))

    def create_screen(self):
        ''' Creates a new screen using fill_new_screen '''
        self.paths_screens()
        self.create_screen_button.click()
        screen_data = PageCreateScreen(self.driver, self.data).fill_new_screen_form()
        self.wait.until(EC.invisibility_of_element_located((By.XPATH, PageScreens.SCREEN_SEARCH_BAR_XPATH)))
        return screen_data

    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        try:
            while True:
                result_search = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, PageScreens.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                if "Loading" not in cad and len(cad) != 0:
                    break

            msg = self.driver.find_element(By.XPATH, PageScreens.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, PageScreens.SCREEN_TABLE_XPATH).value_of_css_property("display")

            if msg == 'none' and table != 'none':
                return True
            else:
                return False
        except TimeoutException:
            return True

    def search_screen(self, screen_name):
        ''' Search for an screen_name: return webElement if this exits and return None if the screen dont exits'''
        self.paths_screens()
        self.screen_search_bar.send_keys(screen_name)

        # Wait until the search ends
        screen_founded = self.search_wait_loading()

        # Iterate through the list to check if the user with user_name is found
        if (screen_founded):
            table_screen = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageScreens.SCREEN_TABLE_XPATH)))
            table_content = table_screen.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                screen = col[0].text
                if (screen == screen_name):
                    # returns the column where the edit and delete buttons are located
                    return col[6]
            return None
        else:
            return None

    def edit_screen(self, element):
        buttons = element.find_elements(By.TAG_NAME, "button")
        buttons[0].click()
        time.sleep(4)
