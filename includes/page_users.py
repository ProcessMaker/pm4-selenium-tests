#!/usr/local/bin/python3
""" Users Page class. """

# Check if using local environment
import sys
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
    CREATE_USER_BUTTON    = "//button[@class='btn btn-secondary']"
    USER_SEARCH_BAR       = "//input[@placeholder='Search']"
    LOADING_MESSAGE_XPATH = "//*[@id='users-listing']/div[2]/div/div[1]"
    USER_TABLE_XPATH      = "//*[@id='users-listing']/div[2]/div/div[2]"
    CONFIRM_DELETE_XPATH  = "//button[text()='Confirm']"
    CANCEL_DELETE_XPATH   = "//button[text()='Cancel']"
    DELETED_USER_FOUND    = "//button[text()='Yes']"
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
        self.user_search_bar        = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        self.create_user_button     = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//text()[contains(.,'User')]/ancestor::button[1]")))
        self.confirm_delete_button  = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.CONFIRM_DELETE_XPATH)))
        self.cancel_delete_button   = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.CANCEL_DELETE_XPATH)))

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
        li=[]
        create_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.CREATE_USER_BUTTON)))
        create_user.click()
        user_name = PageCreateUser(self.driver, self.data).fill_new_user_data(user_data)
        create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']"))).text
        li.append(create_user_succes)
        li.append(user_name)
        return li

    def create_user_personal_dates(self):
        print(True)


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


    def search_user_clear(self):
        searchBox = self.driver.find_element_by_xpath("//*[@id='search']/div/input")
        searchBox.send_keys("")
        self.wait.until(
                EC.text_to_be_present_in_element_value((By.XPATH, "//*[@id='search']/div/input"),''))

    def searchUser(self, user_name):
        ''' Check if an user was created'''

        searchBox = self.driver.find_element_by_xpath("//*[@id='search']/div/input")
        searchBox.send_keys(user_name)
        try:
            self.existUsers = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='users-listing']/div[2]/div/div[1]")))
            print("** " + self.existUsers.text + "**",file=sys.stderr)
            if self.existUsers == 'No Data Available':
                print(user_name +"1 no user found",file=sys.stderr)
                return True
            else:
                print(user_name + "2 ok user found",file=sys.stderr)
                return False
        except TimeoutException:
            print(user_name + "3 ok user found",file=sys.stderr)
        return False

    def search_wait_loading(self, user_name):
        try:
            while True:
                result_search = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                print("** valor del texto es" + cad, file=sys.stderr)
                print(len(cad), file=sys.stderr)
                if "Loading" not in cad  and len(cad) != 0 :
                    print("** resutl final" +  cad, file=sys.stderr)
                    break

            msg   = self.driver.find_element(By.XPATH, PageUsers.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, PageUsers.USER_TABLE_XPATH).value_of_css_property("display")

            print("** mensage" + msg, file=sys.stderr)
            print("** table" + table, file=sys.stderr)
            if msg == 'none':
                print("** usuario encontrado" + msg, file=sys.stderr)
                return True
            else:
                print("** usuario no encontrado" + msg, file=sys.stderr)
                return False
        except:
            print("** user found" + user_name, file=sys.stderr)
            return True

    def search_user(self, user_name):
        ''' Check if an user was created'''
        user_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.USER_SEARCH_BAR)))
        user_search_bar.send_keys(user_name)
        user_founded = self.search_wait_loading(user_name)
        if(user_founded):
            table_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.USER_TABLE_XPATH)))
            table_content = table_user.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')
            print(len(rows), file=sys.stderr)
            for row in rows:
                col  = row.find_elements(By.TAG_NAME, "td") # note: index start from 0, 1 is col 2
                user = col[1].text
                print(user, file=sys.stderr)
                if(user == user_name):
                    print("user founded", file=sys.stderr)
                    return col[8]
            return None
        else:
            return None


    def click_web_element_edit(self, element):
        print("Edit Element", file=sys.stderr)
        butttons = element.find_elements(By.TAG_NAME, "button")
        print(butttons[0], file=sys.stderr)
        butttons[0].click()
        print("llego a edit", file=sys.stderr)


    def delete_user(self, element):
        print("Delete Element", file=sys.stderr)
        butttons = element.find_elements(By.TAG_NAME, "button")
        print(butttons[1], file=sys.stderr)
        butttons[1].click()
        print("llego a delete", file=sys.stderr)
        confirm_deleted_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.CONFIRM_DELETE_XPATH)))
        confirm_deleted_user.click()
        delete_user_succes = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-danger']")))
        return delete_user_succes

    def verify_user_created(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, PageUsers.DELETED_USER_FOUND)))
            return True
        except:
            return False
















