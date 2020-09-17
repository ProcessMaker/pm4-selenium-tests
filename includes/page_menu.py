#!/usr/local/bin/python3
""" Page Navigation class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class PageMenu:
    ''' Page object model for Navigation Menu. '''

    def __init__(self, driver, data):
        ''' Instantiate PageMenu object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(self.driver, 30)

    def paths_menu(self):
        ''' Function to get page elements. '''
        self.avatar = self.wait.until(EC.visibility_of_element_located((By.ID, 'avatarMenu')))
        self.request_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'navbar-request-button')))

    def goto_admin(self):
        ''' Function to navigate to the admin tab. '''
        self.driver.get(self.data['server_url'] + '/admin/users')

    def goto_tasks(self):
        ''' Function to navigate to the request tab. '''
        self.driver.get(self.data['server_url'] + '/tasks')

    def goto_request(self):
        ''' Function to navigate to the request tab. '''
        self.driver.get(self.data['server_url'] + '/requests')
    
    def goto_designer(self):
        ''' Function to navigate to the request tab. '''
        self.driver.get(self.data['server_url'] + '/processes')

    def goto_processes(self):
        ''' Function to navigate to the request tab. '''
        self.driver.get(self.data['server_url'] + 'processes')

    def goto_designer_screen(self):
        ''' Function to navigate to the Screens tab. '''
        self.driver.get(self.data['server_url'] + '/designer/screens')

    def goto_collections(self):
        ''' Function to navigate to the Screens tab. '''
        self.driver.get(self.data['server_url'] + '/collections')

    def log_out(self):
        ''' Logs out the current user '''
        self.paths_menu()
        self.avatar.click()
        self.logout_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li>a[href='/logout']")))
        self.logout_button.click()

    def start_request(self):
        ''' Opens the request popup '''
        self.paths_menu()
        self.request_button.click()
