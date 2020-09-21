#!/usr/local/bin/python3
# Import methods to get environment
from os import getenv
# Check if tests are run on local machine
# Run tests locally with ENVIRONMENT='local' ./path/to/test.py
if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../includes')
    # Import __init__ to include data configuration
    from __init__ import data
# Import BaseTest class where webdriver instance is created
from test_parent import BaseTest
# Import util file where all helper functions are located
import util
from util import read_from_json_file
# Import all page classes
from page import *
# Import Python unittest & regex modules
import unittest, re
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestServerVersions(BaseTest):
    '''  Checking the target server to ensure PM4 and Package versions are up to date '''

    def setUp(self):
        ''' Method to run before each test method. '''
        # Load server url and note step in log
        self.log.append('Load server url')
        self.driver.get(data['server_url'] + '/about')

        # Log in and note step in log
        self.log.append('Log in to server')
        login_page = LoginPage(self.driver, data).login()

        # For use with logs
        self.assertionFailures = []

    def tearDown(self):
        ''' Method to run after each test method. '''
        # Runs final assert check. If assertionFailures list is empty, all assertions
        # passed. If it is not empty, assertions failed.
        self.assertEqual([], self.assertionFailures)

    def test_server_versions(self):
        ''' Verify server & package version numbers '''
        self.log.append('Open "About" Page')
        self.wait.until(EC.visibility_of_element_located((By.ID, 'userMenu')))
        self.log.append('Pull page source\n')
        page_source = self.driver.page_source

        self.log[-1] += 'Check PM4 version: '
        pm4 = read_from_json_file(self.data['repository_path'], '/includes/expected_values.json', 'PM4')
        server_version = re.search(r'(?<=ProcessMaker 4 v)([\d].+)(?:<\/div>)', page_source).group(1)

        try:
            # Verify test case
            self.assertTrue(pm4['Version'] in server_version)
            # Add success message to log if assertion succeeded
            self.log[-1] += 'Correct: ' + server_version

        except AssertionError as e:
            # Add failure message to log if assertion failed
            self.log[-1] += 'Invalid Server Version! Expecting: ' + pm4['Version'] + ' - saw: ' + server_version + '; '
            self.assertionFailures.append(str(e))

        # Retrieve Custom Plugins dictionary from expected_values.json
        pm4_packages = read_from_json_file(self.data['repository_path'], '/includes/expected_values.json', 'Custom Packages')

        # Verify all packages are visible on page with correct version
        packages = [element.text for element in self.driver.find_elements_by_class_name('list-group-item')]

        self.log[-1] += 'Package Versions: '
        for elem in packages:
            for key in pm4_packages.keys():
                if key in elem:
                    try:
                        self.assertTrue(pm4_packages[key]['Version'] in elem)
                        version = re.search(r'(?:Version: )([\d].+)', elem).group(1)
                        #self.log[-1] += 'Correct: ' + key + ' ' + pm4_packages[key]['Version'] + ' ---------- '
                        self.log[-1] += 'Correct: ' + key  + ' Version: ' + pm4_packages[key]['Version'] + ' ---------- '
                    except AssertionError as e:
                        version = re.search(r'(?:Version: )([\d].+)', elem).group(1)
                        #self.log[-1] += 'INVALID: ' + key + ' - Expected: ' + pm4_packages[key]['Version'] + ' ---------- '
                        self.log[-1] += 'INVALID: ' + key + ' Version Seen: ' + version + ' - Expected: ' + pm4_packages[key]['Version'] + ' ---------- '
                        self.assertionFailures.append(str(e))

                    del pm4_packages[key]
                    break

''' Main call. Only used in test file.'''

if __name__ == "__main__":

    ''' Import __main__ to use as parameter for method calls.
    '''
    import __main__

    ''' Assign to data as a key, val pair in order to append relative paths and import files.
    repository_path and data are found in the bootstrap.py file for the Docker container.
    Must be referenced in __main__ call and then passed elsewhere. May be edited elsewhere.

    data['repository_path'] = repository_path
    '''

    ''' You may add any key, value pairs to the data object.

    data comes with:
      data['server_url']
      data['username']
      data['password']
    '''

    ''' output is given back to bootstrap.py after the test is run.
    It is a dictionary with "result" and "message" key, value pairs.
    run_test() is the method that provides this dictionary. It requires the class name,
      the data object, and the __main__ module.
    '''
    output = util.run_test(TestServerVersions, data, __main__)
    print(output)