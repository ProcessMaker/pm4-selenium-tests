#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import string
import util


class PageCreateCategory:
    ''' Page object model for category page'''
    #constants
    CATEGORY_MODAL = "createCategory"
    CATEGORY_NAME = "name"
    CATEGORY_STATUS = "//*[@id='status']"
    CATEGORY_SAVE = "btn-secondary"
    CATEGORY_CANCEL = "btn-outline-secondary"

    
    
    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_create_category(self):
        ''' Function to get page elements. '''
        modal = self.wait.until(EC.visibility_of_element_located((By.ID, self.CATEGORY_MODAL)))
        self.name = modal.find_element_by_id(self.CATEGORY_NAME)
        self.status = Select(modal.find_element_by_xpath(self.CATEGORY_STATUS))
        self.new_category_save = modal.find_element_by_class_name(self.CATEGORY_SAVE)
        self.new_category_cancel = modal.find_element_by_class_name(self.CATEGORY_CANCEL)
    
    def create_categories(self,status):
        self.paths_create_category()
        name = 'category-'+util.generate_text()
        self.name.send_keys(name)
        self.status.select_by_visible_text(status)
        self.new_category_save.click() 
        category_data = {'category_name': name, 'category_status': status}
        return category_data
    
