#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from page_create_category import PageCreateCategory


class PageScreens:
    ''' Page object model for users page'''
    NEW_SCREEN_BUTTON_ID = "create_screen"

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_screens(self):
        ''' Function to get page elements. '''
        self.new_screen_button = self.wait.until(EC.visibility_of_element_located((By.ID, PageScreens.NEW_SCREEN_BUTTON_ID)))

    # tab and buttons
    def create_screen(self):
        ''' Function to click tab processecs. '''
        self.paths_screens()
        self.new_screen_button.click()
