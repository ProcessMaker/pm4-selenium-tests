#!/usr/local/bin/python3
""" Users Page class. """

# Check if using local environment
from os import getenv

from page_create_user import PageCreateUser
from page_user_information import PageUserInformation
from page_menu import PageMenu

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

class PageUsers:
    ''' Page object model for users page'''

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_users(self):
        ''' Function to get page elements. '''
        try:
            self.non_admin_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text() = '12']/following-sibling::td[@class='vuetable-slot'][2]")))
        # Need to run test to find exact exception type
        except:
            pass
        self.user_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        self.create_user_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-secondary']")))

    def search_long_string(self):
        ''' Function to input a long string in the search user bar. '''
        self.paths_users()
        self.user_search_bar.send_keys('qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')
        return (self.user_search_bar.get_property('value') == 'qwertyuiopasdfghjklñzxcvbnmqwertyuiopasdfghjklñzxcvbnmqwerty')

    def edit_non_admin(self):
        ''' Function to edit a non admin user. '''
        self.paths_users()
        self.non_admin_user.click()

    def create_user(self):
        ''' Crerates a new user using fill_new_user '''
        self.paths_users()
        self.create_user_button.click()
        PageCreateUser(self.driver, self.data).fill_new_user()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def create_user_data(self,user_data):
        self.paths_users()
        self.create_user_button.click()
        PageCreateUser(self.driver, self.data).fill_new_user_data(user_data)
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))
        return self.create_user_succes

    def check_users_exists(self):
        ''' Check if there are 2 users, create one if not'''

        # User check
        try:    # changes the non-admin user password if it already exists
            self.non_admin_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text() = '12']/following-sibling::td[@class='vuetable-slot'][2]")))
            PageUsers(self.driver, self.data).edit_non_admin()
            PageUserInformation(self.driver, self.data).change_password()
            PageMenu(self.driver, self.data).goto_request()
            return True

        # Need to run test to find exact exception type
        except TimeoutException:
            PageUsers(self.driver, self.data).create_user()
            PageMenu(self.driver, self.data).goto_request()
            return False

    def wait_for_the_Attribute_value(self, locator, attribute, value):
        try:
            element_attribute = EC._find_element(self.driver, locator).get_attribute(attribute)
            return element_attribute == value
        except StaleElementReferenceException:
            return False
    def search_user(self, user_name):
        ''' Check if an user was created'''
        # self.paths_users()

        self.existUsers = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='users-listing']/div[2]/div/div[1]")))
        print("** " + self.existUsers + "**")
        # self.wait.until(self.wait_for_the_Attribute_value((By.XPATH, '// *[ @ id = "users-listing"] / div[2] / div / div[1]'), "aria-busy", "false"))
        #
        # try:
        #     self.user_search_bar.send_keys(user_name)
        #     element_attribute = EC._find_element(self.driver,By.XPATH, '// *[ @ id = "users-listing"] / div[2] / div / div[1]')
        #     return element_attribute == "display: none;"
        # except StaleElementReferenceException:
        #     return False
        #




