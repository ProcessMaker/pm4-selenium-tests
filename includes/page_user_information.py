#!/usr/local/bin/python3
""" User Info Page class. """
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../includes')
    # Import __init__ to include data configuration
    from __init__ import data

import util

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import string


class PageUserInformation:
    ''' Page object model for user information page'''
    USER_PHONE_ID           = "phone"
    USER_FAX_ID             = "fax"
    USER_CELL_ID            = "cell"
    USER_ADRESS_ID          = "address"
    USER_CITY_ID            = "city"
    USER_STATE_REGION_ID    = "state"
    USER_POSTAL_CODE_ID     = "postal"


    def __init__(self, driver, data):
        ''' Instantiate PageUserInformation object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def paths_user_information(self):
        ''' Function to get page elements. '''
        self.password = self.wait.until(EC.visibility_of_element_located((By.ID, 'password')))
        self.confirm_password = self.wait.until(EC.visibility_of_element_located((By.ID, 'confPassword')))
        self.user_permissions_tab = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#nav-profile']")))

        self.user_language = self.wait.until(EC.visibility_of_element_located((By.ID, "language")))
        self.user_language_deutch = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='de']")))
        self.user_language_english = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='en']")))
        self.user_language_spanish = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='es']")))
        self.user_language_french = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='fr']")))
        self.save_user_information = self.wait.until(EC.visibility_of_element_located((By.ID, 'saveUser')))

        self.user_country = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label[for='country']~select")))
        self.user_afganistan = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AF']")))
        self.user_country_aland_islands = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AX']")))
        self.user_country_albania = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AL']")))
        self.user_country_algeria = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='DZ']")))
        self.user_country_american_samoa = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AS']")))
        self.user_country_andorra = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AD']")))
        self.user_country_angola = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AO']")))
        self.user_country_anguilla = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AI']")))
        self.user_country_antarctica = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AQ']")))
        self.user_country_ntigua_arbuda = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AG']")))
        self.user_country_argentina = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AR']")))
        self.user_country_armenia = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AM']")))
        self.user_country_aruba = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AW']")))
        self.user_country_australia = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AU']")))
        self.user_country_azerbaijan = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AT']")))
        self.user_country_bahamas = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='AZ']")))
        self.user_country_bahrain = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BS']")))
        self.user_country_bangladesh = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BD']")))
        self.user_barbados = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BB']")))
        self.user_country_belarus = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BY']")))
        self.user_country_belgium = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BE']")))
        self.user_country_belize = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BZ']")))
        self.user_country_benin = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BJ']")))
        self.user_country_bermuda = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BM']")))
        self.user_country_bhutan = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BT']")))
        self.user_country_bolivia = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BO']")))
        self.user_country_boznia_herzegovina = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BA']")))
        self.user_country_botzwana = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BW']")))
        self.user_country_bouvet = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BV']")))
        self.user_country_brasil = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BR']")))
        self.user_country_british = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='IO']")))
        self.user_country_brunei = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BN']")))
        self.user_country_bulgaria = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BG']")))
        self.user_country_burkina = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BF']")))
        self.user_country_burundi = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='BI']")))
        self.user_country_cambodia = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value='KH']")))

        self.user_datetime = self.wait.until(EC.visibility_of_element_located((By.ID, "datetime_format")))
        self.user_datetime_dmyhi = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value = 'd/m/Y H:i']")))

        self.user_timezone = self.wait.until(EC.visibility_of_element_located((By.ID, "timezone")))
        self.user_timezone_africa = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "option[value = 'Africa/Abidjan']")))

        # User Profile Information
        self.user_phone     = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_PHONE_ID)))
        self.user_fax       = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_FAX_ID)))
        self.user_cell      = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_CELL_ID)))
        self.user_address   = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_ADRESS_ID)))
        self.user_city      = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_CITY_ID)))
        self.user_state_region  = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_STATE_REGION_ID)))
        self.user_postal_code   = self.wait.until(EC.visibility_of_element_located((By.ID, PageUserInformation.USER_POSTAL_CODE_ID)))


        # Dynamically generated values with util.py
        self.user_phone_val     = util.generate_phone()
        self.user_fax_val       = util.generate_text()
        self.user_cell_val      = util.generate_phone()
        self.user_address_val   = util.generate_text()
        self.user_city_val      = util.generate_text()
        self.user_state_region_val  = util.generate_text()
        self.user_postal_code_val   = util.generate_text()

        self.char_set = string.ascii_letters
        self.user_pass = util.generate_text()

    def page_user_information_wait_visible(self):
        self.paths_user_information()

    def goto_user_permissions(self):
        ''' Click on the user permissions tab'''
        self.paths_user_information()
        self.user_permissions_tab.click()

    def change_user_language(self, selected_language):
        ''' Changes the language for the user to the specified one'''
        self.paths_user_information()
        self.user_language.click()
        self.switch_language(selected_language)

    def switch_language(self, selected_language):
        ''' Switch to click on the language selected'''
        switcher = {
            "deutch": self.user_language_deutch.click(),
            "english": self.user_language_english.click(),
            "spanish": self.user_language_spanish.click(),
            "french": self.user_language_french.click()
        }
        self.save_user_information.click()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def change_password(self):
        ''' Changes the password of the user'''
        self.paths_user_information()
        self.password.send_keys(self.user_pass)
        self.confirm_password.send_keys(self.user_pass)
        self.save_user_information.click()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def change_user_country(self, selected_language):
        ''' Changes the language for the user to the specified one'''
        self.paths_user_information()
        self.user_country.click()
        self.switch_country(selected_language)

    def switch_country(self, selected_language):
        ''' Switch to click on the language selected'''
        switcher = {
            "bolivia": self.user_country_bolivia.click()
        }
        self.save_user_information.click()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def confirm_country(self, selected_language):
        ''' Confirms that a country is the expected one '''
        dropdown = Select(self.driver.find_element_by_css_selector("div[class='form-group col']>select"))
        option = dropdown.first_selected_option
        return (option.text == selected_language)

    def change_user_datetime(self, selected_datetime):
        ''' Changes the language for the user to the specified one'''
        self.paths_user_information()
        self.user_datetime.click()
        self.switch_datetime(selected_datetime)

    def switch_datetime(self, selected_datetime):
        ''' Switch to click on the language selected'''
        switcher = {
            "dmyhi": self.user_datetime_dmyhi.click()
        }
        self.save_user_information.click()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def confirm_datetime(self, selected_datetime):
        ''' Confirms that a country is the expected one '''
        try:    # changes the non-admin user password if it already exists
            if(selected_datetime == "dmyhi"):
                self.selected_country = self.driver.find_element_by_css_selector("option:checked[value='d/m/Y H:i']")       
            return True

        # Need to run test to find exact exception type
        except TimeoutException:
            return False
            

    def change_user_timezone(self, selected_datetime):
        ''' Changes the language for the user to the specified one'''
        self.paths_user_information()
        self.user_timezone.click()
        self.switch_timezone(selected_datetime)

    def switch_timezone(self, selected_datetime):
        ''' Switch to click on the language selected'''
        switcher = {
            "africa": self.user_timezone_africa.click()
        }
        self.save_user_information.click()
        self.create_user_succes = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

    def confirm_timezone(self, selected_datetime):
        ''' Confirms that a country is the expected one '''
        try:    # changes the non-admin user password if it already exists
            if(selected_datetime == "africa"):
                self.selected_country = self.driver.find_element_by_css_selector("option:checked[value='Africa/Abidjan']")       
            return True

        # Need to run test to find exact exception type
        except TimeoutException:
            return False

    def fill_user_information(self):
        ''' Fills in the information fields of a user '''
        self.paths_user_information()
        self.updated_user_succes = self.wait.until(EC.invisibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

        self.user_phone.send_keys(self.user_phone_val)
        self.user_fax.send_keys(self.user_fax_val)
        self.user_cell.send_keys(self.user_cell_val)
        self.user_address.send_keys(self.user_address_val)
        self.user_city.send_keys(self.user_city_val)
        self.user_state_region.send_keys(self.user_state_region_val)
        self.user_postal_code.send_keys(self.user_postal_code_val)
        self.save_user_information.click()
        self.updated_user_succes = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='alert d-none d-lg-block alertBox alert-dismissible alert-success']")))

        #Returns user data information generated
        user_data_information = {'user_phone': self.user_phone_val, 'user_fax':self.user_fax_val,
                                 'user_cell' : self.user_cell_val,  'user_address': self.user_address_val,
                                 'user_city' : self.user_city_val,  'user_state_region': self.user_state_region_val,
                                 'user_postal_code': self.user_postal_code_val}
        return user_data_information

    def get_user_data_information_form(self):
        ''' Get values of the fields of user '''
        self.paths_user_information()

        user_phone =self.user_phone.get_attribute('value')
        user_fax = self.user_fax.get_attribute('value')
        user_cell =self.user_cell.get_attribute('value')
        user_address = self.user_address.get_attribute('value')
        user_city = self.user_city.get_attribute('value')
        user_state_region = self.user_state_region.get_attribute('value')
        user_postal_code = self.user_postal_code.get_attribute('value')

        # Returns user data information of the form
        user_information_form = {'user_phone': user_phone, 'user_fax': user_fax,
                                 'user_cell': user_cell, 'user_address': user_address,
                                 'user_city': user_city, 'user_state_region': user_state_region,
                                 'user_postal_code': user_postal_code}
        return user_information_form

    def verify_user_data_information(self, user_data_information):
        ''' Verify the user data information are equal to the input parameter. Returns True or False'''
        self.paths_user_information()
        user_information_form = self.get_user_data_information_form()

        for key, value in user_data_information.items():
            if key in user_information_form:
                if value != user_information_form[key]:
                    return False
            else:
                return False
        return True