#!/usr/local/bin/python3
""" Screens Page class. """

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys
import os.path

class PageScreens:
    ''' Page object model for screens page'''
    CREATE_SCREEN_BUTTON_ID = "create_screen"
    SCREEN_SEARCH_BAR_XPATH = "//*[@placeholder='Search']"
    LOADING_MESSAGE_XPATH = "//div[@id='screenIndex']/div/following-sibling::div/div[1]"
    SCREEN_TABLE_XPATH = "//div[@id='screenIndex']/div/following-sibling::div/div[2]"
    CONFIRM_DELETE_XPATH = "//button[text()='Confirm']"
    IMPORT_SCREEN_BUTTON_XPATH = "//*[@id='search-bar']/div/div[2]/div[1]/a"

    # XPATH to import a screen
    IMPORT_FILE_INPUT_XPATH = "//*[@id='importScreen']/div/div/div/div[2]/input"
    IMPORT_CONFIRM_SCREEN_XPATH = "//*[@id='importScreen']/div/div/div/div[3]/button[2]"
    LIST_SCREEN_BUTTON_XPATH = "//footer[@id='__BVID__44___BV_modal_footer_']/div/button"

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_screens(self):
        ''' Function to get screen elements. '''
        self.screen_search_bar    = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCREEN_SEARCH_BAR_XPATH)))
        self.create_screen_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.CREATE_SCREEN_BUTTON_ID)))
        self.import_screen_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.IMPORT_SCREEN_BUTTON_XPATH)))

    def create_screen(self):
        ''' Creates a new screen using fill_new_screen '''
        self.paths_screens()
        self.create_screen_button.click()
        # screen_data = PageCreateScreen(self.driver, self.data).fill_new_screen_form()
        # self.wait.until(EC.invisibility_of_element_located((By.XPATH, PageScreens.SCREEN_SEARCH_BAR_XPATH)))

        # with open('drag_and_drop_helper.js') as f:  # getting js as a string from file and assigning to the variable
        #     drag_and_drop_js = f.read()
        #
        #
        # self.driver.execute_script(drag_and_drop_js + "$(\"div[data-cy='controls-FormInput']\").simulateDragDrop({ dropTarget: $(\"div[data-cy='screen-drop-zone']\")});")
        # jq_version = self.driver.execute_script('return $.fn.jquery')
        # print(jq_version, file=sys.stderr)
        # time.sleep(5)

        # return screen_data

    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        try:
            while True:
                result_search = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                if "Loading" not in cad and len(cad) != 0:
                    break

            msg = self.driver.find_element(By.XPATH, self.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, self.SCREEN_TABLE_XPATH).value_of_css_property("display")

            if msg == 'none' and table != 'none':
                return True
            else:
                return False
        except TimeoutException:
            return True

    def search_screen(self, screen_name):
        ''' Search for an screen_name: return webElement if this exits and return None if the screen dont exits'''

        self.paths_screens()
        self.screen_search_bar.send_keys(screen_name)

        # Wait until the search ends
        screen_founded = self.search_wait_loading()

        # Iterate through the list to check if the screen with screen_name is found
        if (screen_founded):
            table_screen = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCREEN_TABLE_XPATH)))
            table_content = table_screen.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                screen = col[0].text
                if (screen == screen_name):
                    # returns the column where the edit and delete buttons are located
                    return col[6]
            return None
        else:
            return None

    def delete_screen(self, element):
        '''Function to delete a screen'''
        buttons = element.find_elements(By.TAG_NAME, "button")
        buttons[4].click()
        confirm_deleted_user = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.CONFIRM_DELETE_XPATH)))
        confirm_deleted_user.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def import_screen(self, file_name):
        '''Function to import to screen on designer'''
        path1 = os.path.dirname(os.path.realpath(__file__))
        path1 = os.path.join(path1, "import")
        file_to_open = os.path.join(path1, file_name)

        self.paths_screens()
        self.import_screen_button.click()
        input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.IMPORT_FILE_INPUT_XPATH)))
        input.send_keys(file_to_open)
        button_import = self.wait.until(EC.presence_of_element_located((By.XPATH, self.IMPORT_CONFIRM_SCREEN_XPATH)))
        button_import.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.LIST_SCREEN_BUTTON_XPATH)))