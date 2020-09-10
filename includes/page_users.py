#!/usr/local/bin/python3
""" Users Page class. """

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../../includes')
    # Import __init__ to include data configuration
    from __init__ import data

from page_create_user import PageCreateUser
from page_user_information import PageUserInformation
from page_menu import PageMenu


from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class PageUsers:
    ''' Page object model for users page'''
    CREATE_USER_BUTTON_XPATH = "//button[@class='btn btn-secondary']"
    USER_SEARCH_BAR_XPATH    = "//input[@placeholder='Search']"
    LOADING_MESSAGE_XPATH    = "//*[@id='users-listing']/div[2]/div/div[1]"
    USER_TABLE_XPATH         = "//*[@id='users-listing']/div[2]/div/div[2]"
    CONFIRM_DELETE_XPATH     = "//button[text()='Confirm']"
    CANCEL_DELETE_XPATH      = "//button[text()='Cancel']"
    DELETED_USER_FOUND       = "//button[text()='Yes']"

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
        user_data = PageCreateUser(self.driver, self.data).fill_new_user()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))
        return user_data

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

    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        try:
            while True:
                result_search = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, PageUsers.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                if "Loading" not in cad and len(cad) != 0:
                    break

            msg = self.driver.find_element(By.XPATH, PageUsers.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, PageUsers.USER_TABLE_XPATH).value_of_css_property("display")

            if msg == 'none' and table != 'none':
                return True
            else:
                return False
        except:
            return True

    def search_user(self, user_name):
        ''' Search for an user_name: return webElement if this exits and return None if the user dont exits'''

        self.paths_users()
        self.user_search_bar.send_keys(user_name)

        # Wait until the search ends
        user_founded = self.search_wait_loading()

        # Iterate through the list to check if the user with user_name is found
        if (user_founded):
            table_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.USER_TABLE_XPATH)))
            table_content = table_user.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                user = col[1].text
                if (user == user_name):
                    #returns the column where the edit and delete buttons are located
                    return col[8]
            return None
        else:
            return None
"""
    def searchUser(self, findName):
        ''' Search some user'''
        self.paths_users()
        self.user_search_bar.send_keys(findName)
        try:
            existUsers = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='users-listing']/div[2]/div/div[1]")))
            #validate option
            userTest = existUsers.value_of_css_property("display")
            print(userTest)
            if userTest == 'block':
                return True
            else:
                return False
        except TimeoutException:
            return False


    def create_new_user(self, username, password, email, status):                                                                              
        ''' Create an inactive user'''
        self.paths_users()
        self.create_user_button.click()
        PageCreateUser(self.driver, data).fill_data_user(username, password, email, status)
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def verifyUser(self):
        # new user information
        username = 'userAutomation'+generate_text()
        password = generate_randomPassword(8)
        email = generate_email()
        status = 'active'

        # Validate if the user exists
        noExistUser = PageUsers(self.driver, data).searchUser(username)
        if noExistUser == True:
            # Create an user if not exist
            PageUsers(self.driver, data).create_new_user(username, password, email, status)
        return [username, password]
"""