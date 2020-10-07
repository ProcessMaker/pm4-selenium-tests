#!/usr/local/bin/python3
""" Collections Page class. """
import os.path
import sys
from page_create_collection import PageCreateCollection

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class PageCollection:
    ''' Page object model for collections page'''
    CREATE_COLLECTION_BUTTON_ID = "addUserCollection"
    COLLECTION_SEARCH_BAR_XPATH = "//*[@placeholder='Search']"
    COLLECTION_TABLE_XPATH = "//*[@id='collectionIndex']/div[2]/div"
    NO_DATA_AVAILABLE_XPATH = "//tbody/child::tr/td[@class='vuetable-empty-result']"
    CONFIRM_DELETE_COLLECTION_ID = "confirm"
    IMPORT_COLLECTION_BUTTON_ID = "import_collection"

    def __init__(self, driver, data):
        ''' Instantiate PageCollection object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_collection(self):
        ''' Function to get page elements. '''
        self.create_collection_button = self.wait.until(EC.visibility_of_element_located((By.ID, PageCollection.CREATE_COLLECTION_BUTTON_ID)))
        self.collection_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCollection.COLLECTION_SEARCH_BAR_XPATH)))
        self.import_collection_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.IMPORT_COLLECTION_BUTTON_ID)))

    def create_new_collection(self, edit_screen, display_screen):
        ''' Function to create a new collection. '''
        self.paths_collection()

        self.create_collection_button.click()
        collection_data = PageCreateCollection(self.driver, self.data).fill_new_collection(edit_screen, display_screen)
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "addUserCollection")))
        return collection_data

    def goto_collection_home(self):
        collection_home = None
        try:
            collection_home = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Collections')]")))
        except TimeoutException:
            collection_home = self.driver.find_element((By.XPATH, "//a[contains(text(),'Collections')]"))
        collection_home.click()

    def wait_search_collection(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCollection.NO_DATA_AVAILABLE_XPATH)))
            return False
        except TimeoutException:
            return True

    def search_collection(self, name_collection):
        ''' Function to search a collection. '''
        self.paths_collection()
        self.collection_search_bar.send_keys(name_collection)
        result_search = self.wait_search_collection()

        if result_search:
            table_collection = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCollection.COLLECTION_TABLE_XPATH)))
            table_content = table_collection.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                collection = col[1].text
                if collection == name_collection:
                    # returns the column where the edit and delete buttons are located
                    return col[7]
            return None
        else:
            return None

    def select_collection(self, element):
        ''' Function to select an collection. '''
        buttons = element.find_elements(By.TAG_NAME, "button")
        buttons[0].click()

    def delete_collection(self, element):
        ''' Function to deleted a collection. '''
        buttons = element.find_elements(By.TAG_NAME, "button")
        buttons[2].click()
        confirm_deleted_collection = self.wait.until(
            EC.visibility_of_element_located((By.ID, PageCollection.CONFIRM_DELETE_COLLECTION_ID)))
        confirm_deleted_collection.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, PageCollection.COLLECTION_TABLE_XPATH)))

    def import_collection(self, path):
        '''Function to import a collection'''
        self.paths_collection()
        self.import_collection_button.click()
        file_name = 'automation_trogdor_collection001.json'
        # print(os.path.abspath(file_name), file=sys.stderr)
        path1 = '"'+os.path.realpath(__file__)+'"'
        # print("La ruta de inlcudes ", file=sys.stderr)
        # print(path1, file=sys.stderr)
        return path1

        # input = self.wait.until(EC.presence_of_element_located(
        #     (By.XPATH, "//*[@id='importCollection']/div/div/div/div[2]/input")))
        # input.send_keys("")
        # button_import = self.wait.until(EC.presence_of_element_located(
        #     (By.XPATH,"//*[@id='importCollection']/div/div/div/div[3]/button[2]")))
        # button_import.click()
        # time.sleep(10)
