#!/usr/local/bin/python3
# functions for the POM POC

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class PageUsers:
    ''' Page object model for users page'''

    def __init__(self, driver, data):
        self.driver=driver
        self.data=data
        self.wait = WebDriverWait(driver, 30)
    
    def paths_users(self):
        self.user_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']"))) 
        self.non_admin_edit = self.wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@title='Edit'])[2]"))) 

    def search_long_string(self):
        self.paths_users()
        self.user_search_bar.send_keys('qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')
        return (self.user_search_bar.get_property('value') == 'qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty') 

    def edit_non_admin(self):
        self.paths_users()
        self.non_admin_edit.click()