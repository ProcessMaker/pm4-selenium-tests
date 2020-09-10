#!/usr/local/bin/python3

# Check if using local environment

from util import generate_text

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class PageNewSavedsearch:
    ''' Page object model for Login Page. '''

    NEW_SAVEDSEARCH_WINDOW_ID = "save-search-modal___BV_modal_content_"

    NEW_SAVEDSEARCH_NAME_XPATH = "//small[text() = 'The name of this saved search.']/preceding-sibling::input"

    NEW_SAVEDSEARCH_ICON_CSS = "span[class='multiselect__single']"
    NEW_SAVEDSEARCH_ICON_LENS_XPATH = "//div[@class='multiselect-icons']/div/div/div/ul/li"

    NEW_SAVEDSEARCH_USERS_XPATH = "//legend[text() = 'Share With Users']/following::div[@class='bv-no-focus-ring']"
    NEW_SAVEDSEARCH_USERS_ADMIN_XPATH = "(//span[text() = 'User Admin'])[3]"

    NEW_SAVEDSEARCH_GROUPS_XPATH = "//legend[text() = 'Share With Groups']/following::div[@class='bv-no-focus-ring']"
    NEW_SAVEDSEARCH_GROUPS_ADMINISTRATOR = "(//span[text() = 'Administrators'])"

    NEW_SAVEDSEARCH_SAVE_CSS = "button[class= 'btn btn-secondary']"

    NEW_SAVEDSEARCH_TABLE_CSS = "div[class= 'jumbotron jumbotron-fluid']"
    

    def __init__(self, driver, data):
        ''' Instantiate PageLogin class. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_new_savessearch(self):
        ''' Function to get page elements. '''
        self.new_savedsearch_window = self.wait.until(EC.visibility_of_element_located((By.ID, PageNewSavedsearch.NEW_SAVEDSEARCH_WINDOW_ID)))

        self.new_savedsearch_name = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewSavedsearch.NEW_SAVEDSEARCH_NAME_XPATH)))

        self.new_savedsearch_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewSavedsearch.NEW_SAVEDSEARCH_ICON_CSS)))

        self.new_savedsearch_users = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewSavedsearch.NEW_SAVEDSEARCH_USERS_XPATH)))

        self.new_savedsearch_groups = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewSavedsearch.NEW_SAVEDSEARCH_GROUPS_XPATH)))

        self.new_savedsearch_save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewSavedsearch.NEW_SAVEDSEARCH_SAVE_CSS)))

        
    def create_new_savedsearch(self):
        ''' Function to navigate to Login page. '''
        name = generate_text()
        self.paths_new_savessearch()
        self.new_savedsearch_name.send_keys(name)

        self.new_savedsearch_icon.click()
        self.new_savedsearch_icon_lens = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewSavedsearch.NEW_SAVEDSEARCH_ICON_LENS_XPATH)))
        self.new_savedsearch_icon_lens.click()

        self.new_savedsearch_users.click()
        self.new_savedsearch_user_admin = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewSavedsearch.NEW_SAVEDSEARCH_USERS_ADMIN_XPATH)))
        self.new_savedsearch_user_admin.click()

        self.new_savedsearch_groups.click()
        self.new_savedsearch_group_administrator = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageNewSavedsearch.NEW_SAVEDSEARCH_GROUPS_ADMINISTRATOR)))
        self.new_savedsearch_group_administrator.click()

        self.new_savedsearch_save.click()

        self.new_savedsearch_table = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageNewSavedsearch.NEW_SAVEDSEARCH_TABLE_CSS)))

        return(name)
