#!/usr/local/bin/python3
""" New Create Collection Page class. """
import util
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys

class PageCreateCollection:
    ''' Page object model for create collection page'''
    NAME_TEXT_ID = "name"
    DESCRIPTION_TEXTAREA_ID = "description"
    CREATESCREEN_LIST_XPATH = "//label[@for='create_screen_id']/following-sibling::div"
    VIEWSCREEN_LIST_XPATH = "//label[@for='read_screen_id']/following-sibling::div"
    EDITSCREEN_LIST_XPATH = "//label[@for='update_screen_id']/following-sibling::div"
    SAVE_COLLECTION_BUTTON_XPATH = "//button[contains(text(),'Save')]"

    def __init__(self, driver, data):
        ''' Instantiate PageCreateCollection object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 30)

    def paths_create_collection(self):
        ''' Function to get page elements. '''
        self.name_text = self.wait.until(EC.visibility_of_element_located((By.ID, PageCreateCollection.NAME_TEXT_ID)))
        self.description_textarea = self.wait.until(EC.visibility_of_element_located((By.ID, PageCreateCollection.DESCRIPTION_TEXTAREA_ID)))
        self.create_screen_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateCollection.CREATESCREEN_LIST_XPATH)))
        self.view_screen_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateCollection.VIEWSCREEN_LIST_XPATH)))
        self.edit_screen_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateCollection.EDITSCREEN_LIST_XPATH)))
        self.save_collection_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageCreateCollection.SAVE_COLLECTION_BUTTON_XPATH)))

        # Dynamically generated values with util.py
        self.name_text_val = util.generate_text()
        self.description_textarea_val = util.generate_text()

    def select_create_screen(self, screen_edit):
        self.create_screen_list.click()
        input_create_screen = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//label[@for='create_screen_id']/following-sibling::div/div[@class='multiselect__tags']/input")))
        input_create_screen.send_keys(screen_edit)
        input_create_screen.send_keys(Keys.ENTER)


    def select_view_screen(self, screen_display):
        self.view_screen_list.click()
        view_edit_screen = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//label[@for='read_screen_id']/following-sibling::div/div[@class='multiselect__tags']/input")))
        view_edit_screen.send_keys(screen_display)
        view_edit_screen.send_keys(Keys.ENTER)


    def select_edit_screen(self, screen_edit):
        self.edit_screen_list.click()
        input_edit_screen = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//label[@for='update_screen_id']/following-sibling::div/div[@class='multiselect__tags']/input")))
        input_edit_screen.send_keys(screen_edit)
        input_edit_screen.send_keys(Keys.ENTER)
        self.description_textarea.click()


    def fill_new_collection(self, screen_edit, screen_display):
        ''' Fills the fields of a new user'''
        self.paths_create_collection()
        self.name_text.send_keys(self.name_text_val)
        self.description_textarea.send_keys(self.description_textarea_val)

        self.select_create_screen(screen_edit)
        self.select_view_screen(screen_display)
        if ("type here to search" in self.create_screen_list.text):
            self.select_create_screen(screen_edit)

        self.select_edit_screen(screen_edit)
        if ("type here to search" in self.view_screen_list.text):
            self.select_view_screen(screen_display)
        if ("type here to search" in self.edit_screen_list.text):
            self.select_edit_screen(screen_edit)

        self.save_collection_button.click()
        collection_data = {'collection_name': self.name_text_val, 'collection_description': self.description_textarea_val,
                           'collection_create_screen': 'Edit Form', 'collection_view_screen': 'View Form',
                           'collection_edit_screen': 'Edit Form'}
        return collection_data
