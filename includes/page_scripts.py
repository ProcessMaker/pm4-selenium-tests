#!/usr/local/bin/python3
""" Users Page class. """
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_create_scripts import PageCreateScript
from page_scripts_builder import PageScriptsBuilder


class PageScripts:
    ''' Page object model for users page'''
    TAB_SCRIPTS_CSS = "a[id='nav-sources-tab']"
    TAB_CATEGORIES_CSS = "a[id='nav-categories-tab']"
    BUTTON_NEW_SCRIPTS_CSS = "a[id='create_script']"
    SCRIPTS_SEARCH_BAR_XPATH = "(//input[@placeholder='Search'])"

    LOADING_MESSAGE_XPATH = "//*[@id='scriptIndex']/div[2]/div/div[1]"
    SCRIPT_TABLE_XPATH = "//*[@id='scriptIndex']/div[2]/div/div[2]"
    CONFIRM_DELETE_SCRIPT_XPATH = "//button[text()='Confirm']"

    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_scripts(self):
        ''' Function to get page elements. '''
        self.tab_scripts = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TAB_SCRIPTS_CSS)))
        self.categories = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.TAB_CATEGORIES_CSS)))

    # tab and buttons
    def tab_scripts(self):
        ''' Function to click tab processecs. '''
        self.paths_scripts()
        self.tab_scripts.click()
        self.btn_new_scripts = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.BUTTON_NEW_SCRIPTS_CSS)))
        self.scripts_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCRIPTS_SEARCH_BAR_XPATH)))

    def create_scripts(self, description, category, language, runScript, timeout):
        ''' Function to create a category. '''
        self.tab_scripts()
        self.btn_new_scripts.click()
        # create a new script
        script_data = PageCreateScript(self.driver, self.data).create_scripts(description, category, language, runScript, timeout)
        PageScriptsBuilder(self.driver, self.data).paths_create_scripts_builder()
        return script_data

    def search_wait_loading(self):
        ''' Verify if the search was finished'''
        try:
            while True:
                result_search = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, self.LOADING_MESSAGE_XPATH)))
                cad = result_search.text
                if "Loading" not in cad and len(cad) != 0:
                    break

            msg = self.driver.find_element(By.XPATH, self.LOADING_MESSAGE_XPATH).value_of_css_property("display")
            table = self.driver.find_element(By.XPATH, self.SCRIPT_TABLE_XPATH).value_of_css_property("display")

            if msg == 'none' and table != 'none':
                return True
            else:
                return False
        except TimeoutException:
            return True

    def search_script(self, script_name):
        ''' Search for a script_name: return webElement if this exits and return None if the script doesn't exit'''
        self.scripts_search_bar = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCRIPTS_SEARCH_BAR_XPATH)))
        self.scripts_search_bar.send_keys(script_name)

        # Wait until the search ends
        scritpt_founded = self.search_wait_loading()

        # Iterate through the list to check if the script with script_name is found
        if (scritpt_founded):
            table_script = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCRIPT_TABLE_XPATH)))
            table_content = table_script.find_element(By.TAG_NAME, 'tbody')
            rows = table_content.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                col = row.find_elements(By.TAG_NAME, "td")
                script = col[0].text
                if (script == script_name):
                    # returns the column where the edit and delete buttons are located
                    return col[6]
            return None
        else:
            return None

    def delete_script(self, element):
        '''Function to delete a script'''
        buttons = element.find_elements(By.TAG_NAME, "button")
        buttons[3].click()
        confirm_deleted_script = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.CONFIRM_DELETE_SCRIPT_XPATH)))
        confirm_deleted_script.click()
        delete_script_succes = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))
