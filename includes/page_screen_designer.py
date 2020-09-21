#!/usr/local/bin/python3
""" Screens designer Page class. """
import sys

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver import ActionChains

class PageScreenDesigner:
    ''' Page object model for screens designer page'''
    # LINEINPUT_CONTROL_XPATH   = "//text()[contains(.,'Line Input')]/ancestor::div[1]"
    LINEINPUT_CONTROL_XPATH = "//*[@id='controls']/div[6]"
    CONTENT_DRAG_XPATH        = "//*[@id='screen-container']/div[3]"
    SAVE_VERSION_BUTTON_XPATH = "//button[@title='Save Versions']"
    SAVE_BUTTON_XPATH         = "//button[text()='Save']"

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_screen_designer(self):
        ''' Function to get screen designer elements. '''
        self.input_control   = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageScreenDesigner.LINEINPUT_CONTROL_XPATH)))
        self.content_drag    = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageScreenDesigner.CONTENT_DRAG_XPATH)))
        self.save_versions_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageScreenDesigner.SAVE_VERSION_BUTTON_XPATH)))

    def drag_and_drop_input(self):
        self.paths_screen_designer()
        action = ActionChains(self.driver)
        # action.drag_and_drop(self.input_control, self.content_drag).perform()
        action.click(self.content_drag).drag_and_drop(self.input_control, self.content_drag).perform()
        return True

    def save_versions(self):
        self.paths_screen_designer()
        self.save_versions_button.click()
        save_confirm = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageScreenDesigner.SAVE_BUTTON_XPATH)))
        save_confirm.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))





