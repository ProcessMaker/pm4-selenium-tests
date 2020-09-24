#!/usr/local/bin/python3

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import string
import util
from selenium import webdriver

class PageScriptsBuilder:
    ''' Page object model for category page'''
    # constants    
    SCRIPT_BUILD_CODE_CSS = "div[class='view-lines']"
    SCRIPT_BUILD_XPATH = "//span[contains(text(),'[];')]"
    SCRIPT_BUILD_BUTTON_RUN_CSS = "button[class='btn text-capitalize pl-3 pr-3 btn-secondary btn-sm']"
    SCRIPT_BUILD_OUTPUT_CSS = "div[class='output text-white']"
    SCRIPT_BUILD_SAVE_CSS = "div.p-0>button"


    def __init__(self, driver, data):
        ''' Instantiate PageProcesses object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 60)

    def paths_create_scripts_builder(self):
        ''' Function to get page elements. '''
        self.code = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_CODE_CSS)))
        self.button_run = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_BUTTON_RUN_CSS)))
        self.output = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.SCRIPT_BUILD_OUTPUT_CSS)))
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

      #3  wa = WebDriverWait(self.driver, 30)
        self.button_save.click()
#################
        title =  self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"input.form-control"))).send_keys('1')
        title2 =  self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"textarea.form-control"))).send_keys('1')
        save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div.modal-body>div.modal-footer>button.btn.btn-secondary")))
        save.click()
#################

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))
        
        self.button_run.click()


        resp='{"output": "smoke test"}'

        #code1 = self.wait.until(EC.visibility_of_element_located((By.XPATH,'//samp[contains(text(),'+resp+')]')))
        code1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"pre.text-white>samp")))
        
        print(code1)
             
        script_code = {
            'script_builder_code': code1
            }
        return script_code
