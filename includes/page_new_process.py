#!/usr/local/bin/python3
""" Page Navigation class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from util import generate_text


class PageNewProcess:
    ''' Page object model for Navigation Menu. '''

    PROCESS_POPUP_XPATH = "//h5[text()='Create Process']"
    PROCESS_NAME_CSS = "input[name='name']"
    PROCESS_DESCRIPTION_CSS = "textarea[name='description']"

    PROCESS_CATEGORY_CSS = "div[class='multiselect__tags']"
    PROCESS_ANY_CATEGORY_CSS = "li[class='multiselect__element']"

    PROCESS_SAVE_CSS = "div[class='modal-footer']>button[class='btn btn-secondary']"
    PROCESS_CANVAS_ID = "modeler-app"

    def __init__(self, driver, data):
        ''' Instantiate PageMenu object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(self.driver, 30)

    def paths_menu(self):
        ''' Function to get page elements. '''
        self.process_popup = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewProcess.PROCESS_POPUP_XPATH)))
        self.process_name = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewProcess.PROCESS_NAME_CSS)))
        self.process_description = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewProcess.PROCESS_DESCRIPTION_CSS)))

        self.process_category = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewProcess.PROCESS_CATEGORY_CSS)))

        self.process_save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewProcess.PROCESS_SAVE_CSS)))

    def fill_new_process(self, category, name):
        ''' Logs out the current user '''

        self.paths_menu()
        self.process_name.send_keys(name + ": Process Self Service")
        self.process_description.send_keys("Test Selfservice Smoke test")    

        self.process_category.click()
        self.process_any_category = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewProcess.PROCESS_ANY_CATEGORY_CSS)))
        if(category == 'any'):
            self.process_any_category.click()    
        
        if(category != 'any'):
            self.process_category.click()
            self.process_any_category = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewProcess.PROCESS_ANY_CATEGORY_CSS)))
            self.process_any_category.click()

        self.process_save.click()
        self.process_canvas = self.wait.until(EC.visibility_of_element_located((By.ID, PageNewProcess.PROCESS_CANVAS_ID)))
        return (self.process_canvas.is_enabled())
