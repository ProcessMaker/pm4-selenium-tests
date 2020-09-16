#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from page_create_category import PageCreateCategory

class PageProcesses:
    ''' Page object model for users page'''
    TAB_PROCESSES_CSS = "a[id='nav-sources-tab']"
    BUTTON_NEW_PROCESS_ID = "create_process"

    TAB_CATEGORIES = "//*[@id='nav-categories-tab']"
    TAB_ARCHIVED_PROCESSES = "//*[@id='nav-archived-tab']"
    BTN_CREATE_CATEGORY = "//*[@id='create_category']"

    CATEGORY_SEARCH_BAR_XPATH = "(//input[@placeholder='Search'])[2]" #"//input[@placeholder='Search']"
    LOADING_MESSAGE_XPATH = "//*[@id='categories-listing']/div[2]/div[1]"
    CATEGORY_TABLE_XPATH  = "//*[@id='categories-listing']/div[2]/div[2]"
    
    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_processes(self):
        ''' Function to get page elements. '''
        self.processes = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TAB_PROCESSES_CSS)))
        self.categories = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.TAB_CATEGORIES)))
        self.archive_processes = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.TAB_ARCHIVED_PROCESSES)))
    
    # buttons sidebar left
    def goto_processes(self):
        ''' Function to go to scripts. '''
        self.driver.get(self.data['server_url'] + '/processes')

    def goto_scripts(self):
        ''' Function to go to scripts. '''
        self.driver.get(self.data['server_url'] + '/designer/scripts')
    
    def goto_screens(self):
        ''' Function to go to screens. '''
        self.driver.get(self.data['server_url'] + '/designer/screens')

    def goto_environment_varibles(self):
        ''' Function to go to environment variables. '''
        self.driver.get(self.data['server_url'] + '/designer/environment-variables')
    # tab and buttons
    def tab_processes(self):
        ''' Function to click tab processecs. '''
        self.paths_processes()
        self.processes.click()
    
    def tab_categories(self):        
        ''' Function to click tab categories. '''
        self.paths_processes()        
        self.categories.click()
        self.btnCategory = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.BTN_CREATE_CATEGORY)))
        self.category_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.CATEGORY_SEARCH_BAR_XPATH)))
        
    def tab_archived_processes(self):
        ''' Function to click tab archive processes. '''
        self.paths_processes()
        self.archive_processes.click()  
    
    def create_process(self):
        ''' Function to create a category. '''
        self.paths_processes()
        self.new_process_button.click()

    def create_category(self, status):
        ''' Function to create a category. '''
        self.paths_processes()
        self.tab_categories()
        self.btnCategory.click()
        # status = Active or Inactive
        category_data = PageCreateCategory(self.driver,self.data).create_categories(status)
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))
        return category_data
    
    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        try:
            while True:
                result_search = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, PageProcesses.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                if "Loading" not in cad and len(cad) != 0:
                    break

            msg = self.driver.find_element(By.XPATH, PageProcesses.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, PageProcesses.CATEGORY_TABLE_XPATH).value_of_css_property("display")

            if msg == 'none' and table != 'none':
                return True
            else:
                return False
        except:
            return True


    def search_category(self, category_name):
        ''' Search for a category_name: return webElement if this exits and return None if the category doesn't exit'''

        self.paths_processes()
        self.category_search_bar.send_keys(category_name)

        # Wait until the search ends
        category_founded = self.search_wait_loading()
        
        # Iterate through the list to check if the user with user_name is found
        if (category_founded):
            table_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcesses.CATEGORY_TABLE_XPATH)))
            table_content = table_user.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                category = col[0].text
                if (category == category_name):
                    #returns the column where the edit and delete buttons are located
                    return col[0]
            return None
        else:
            return None
