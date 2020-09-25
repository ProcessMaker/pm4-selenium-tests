#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import string
import util
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
SCRIPT_CODE = """
<?php  
return "smoke";
"""

class PageScriptsBuilder:
    ''' Page object model for category page'''
    # constants    
    SCRIPT_BUILD_CODE_CSS = "div[class='view-lines']"
    SCRIPT_BUILD_XPATH = "//span[contains(text(),'[];')]"
    SCRIPT_BUILD_BUTTON_RUN_CSS = "button[class='btn text-capitalize pl-3 pr-3 btn-secondary btn-sm']"
    SCRIPT_BUILD_OUTPUT_CSS = "div[class='output text-white']"
    SCRIPT_BUILD_SAVE_CSS = "div.p-0>button"


    FINISH_LOADING_SCRIPT_XPATH = "//i[@class='fas fa-check text-success']"


    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_create_scripts_builder(self):
        ''' Function to get page elements. '''
        # self.code = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_CODE_CSS)))
        self.button_run = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_BUTTON_RUN_CSS)))
        # self.output = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_OUTPUT_CSS)))
        self.button_save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_SAVE_CSS)))
        
    def create_scripts_builder(self, code):
        self.paths_create_scripts_builder()     

        elem = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.SCRIPT_BUILD_XPATH)))
        self.driver.execute_script("""
                                    var elem = arguments[0];
                                    console.log(elem); 
                                    elem.innerHTML = '&nbsp;'
                                    elem.parentElement.innerHTML += '<span class="mtk20">"smoke&nbsp;test"</span><span class="mtk1">;</span>'
        """, elem)
        time.sleep(11)

        self.save_script_builder()
        # self.run_script_builder()
        #
        # #code1 = self.wait.until(EC.visibility_of_element_located((By.XPATH,'//samp[contains(text(),'+resp+')]')))
        # code1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"pre.text-white>samp")))
        # print("This is the code1", file=sys.stderr)
        # print(code1.text, file=sys.stderr)
        script_code = {
            'script_builder_code': 'code1.text'
            }
        return script_code

    def save_script_builder(self):
        self.paths_create_scripts_builder()
        self.button_save.click()
        save = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.modal-body>div.modal-footer>button.btn.btn-secondary")))
        save.click()
        save_script_succes = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def run_script_builder(self):
        self.button_run.click()
        wait = WebDriverWait(self.driver, 200)
        wait.until(EC.visibility_of_element_located((By.XPATH, PageScriptsBuilder.FINISH_LOADING_SCRIPT_XPATH)))

    def put_text(self):
        textarea =self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id='script-container']/div/div/div[2]/div/div[1]/div/div/div[1]/textarea")))
        textarea.send_keys(Keys.CONTROL + "a")
        textarea.send_keys(Keys.DELETE)
        textarea.send_keys(SCRIPT_CODE)
        # print('el texto es :', textarea.get_property('value'))
        # print('el texto es 2 :', textarea.text)

        time.sleep(5)
