#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from page_create_category import PageCreateCategory

from util import generate_text
from selenium.webdriver import ActionChains


class PageScreenCanvas:
    ''' Page object model for users page'''
    FILE_PREVIEW_ORIGIN_CSS = "i[class='fas fa-file-image']"

    SAVE_CSS = "button[class='btn btn-secondary']"

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_screen_canvas(self):
        ''' Function to get page elements. '''
        self.file_preview_origin = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageScreenCanvas.FILE_PREVIEW_ORIGIN_CSS)))


    # tab and buttons
    def drag_n_drop(self):
        ''' Function to click tab processecs. '''
        self.paths_screen_canvas()
        
        action = ActionChains(self.driver)

        #action.drag_and_drop_by_offset(self.file_preview_origin, 500, 500)
        
        self.driver.execute_script("new Actions(driver).dragAndDropBy(dragElementFrom, 100, 0).build() .perform();")