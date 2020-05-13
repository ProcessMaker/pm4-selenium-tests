#!/usr/local/bin/python3
""" Module to contain helper functions that cut down on redundant code in main calls.
"""

import unittest
from contextlib import redirect_stdout
from io import StringIO
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def run_test(classname, data, modulename):
    ''' Function to run test and redirect output from stdout
        and return results in PM4 output variable.
    '''
    if data is {}:
        return 'data dictionary must not be empty'

    if not classname:
        return 'classname missing'

    if not data:
        return 'data missing'

    if not modulename:
        return 'modulename missing'

    suite = unittest.TestLoader().loadTestsFromModule(modulename)
    classname.data = data
    with StringIO() as buffer:
        with redirect_stdout(buffer):
            unittest.TextTestRunner(stream=buffer).run(suite)
            return {"result": parse_results(buffer.getvalue())}

def parse_results(buffer):
    ''' Function to parse the unittest results into PM4-friendly format.
    '''
    if not buffer or buffer is '':
        return 'No unittest result detected'

    if buffer.startswith('.'):
        return 'SUCCESS'
    elif buffer.startswith('E'):
        return 'FAIL'
    else:
        return 'Test failed to execute'

def login(url, workspace, username, password, driver):
    ''' Function to log user in to workspace.
    '''
    # Navigate to server
    driver.get(url)

    # Select and submit workspace
    driver.find_element_by_id('display_select_input').click()
    driver.find_element_by_link_text(workspace).click()
    driver.find_element_by_id('sentworkspace').click()

    # Wait for login page to load
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((By.ID, 'form[BSUBMIT]')))

    # Login
    driver.find_element_by_id('form[USR_USERNAME]').send_keys(username)
    driver.find_element_by_id('form[USR_PASSWORD_MASK]').send_keys(password)
    driver.find_element_by_id('form[BSUBMIT]').click()

    return driver
