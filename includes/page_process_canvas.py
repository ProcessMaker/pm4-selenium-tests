#!/usr/local/bin/python3
""" Users Page class. """

# Check if using local environment
from os import getenv

if getenv('ENVIRONMENT') == 'local':
    # Import sys.path to add the /includes directory to the path
    # This matches the docker executor's path so local test imports match
    # remote Trogdor test imports
    from sys import path
    path.append('../../includes')
    # Import __init__ to include data configuration
    from __init__ import data

from page_create_user import PageCreateUser
from page_user_information import PageUserInformation
from page_menu import PageMenu


from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.action_chains import ActionChains


class PageProcessCanvas:
    ''' Page object model for users page'''
    CANVAS_CSS = "DIV[CLASS='paper-container h-100 pr-4 col']"
    START_EVENT_ORIGIN_CSS = "div[title='Start Event']"
    TASK_ORIGIN_CSS = "div[title='Task']"
    END_EVENT_ORIGIN_CSS = "div[title='End Event']"

    START_EVENT_XPATH = "//*[name()='g' and contains(@data-type,'processmaker.components.nodes.startEvent.Shap')]"
    TASK_XPATH = "//*[name()='g']/*[name()='g' and contains(@data-type,'processmaker.components.nodes.task.Shape')]"
    END_XPATH = "//*[name()='g' and contains(@data-type,'processmaker.components.nodes.endEvent.Shap')]"

    SAVE_BUTTON_CSS = "button[title='Save']"
    COMMIT_SAVE_CSS = "div[class='modal-footer']>button[class='btn btn-secondary']"
    SAVE_ALERT_CSS = "div[class='alert d-none d-lg-block alertBox alert-dismissible alert-success']"

    FLOW_ID = "sequence-flow-button"

    def __init__(self, driver, data):
        ''' Instantiate PageUsers object. '''
        self.driver = driver
        self.data = data
        self.wait = WebDriverWait(driver, 10)

    def path_process_canvas(self):
        ''' Function to get page elements. '''
        self.canvas = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.CANVAS_CSS)))
        self.start_event_origin = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.START_EVENT_ORIGIN_CSS)))
        self.task_event_origin = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.TASK_ORIGIN_CSS)))
        self.end_event_origin = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.END_EVENT_ORIGIN_CSS)))

        self.save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.SAVE_BUTTON_CSS)))

    def drag_n_drop(self, element, horizontal_offset, vertical_offset):
        ''' Takes an horizontal and vertical offset. '''
        self.path_process_canvas()

        action = ActionChains(self.driver)

        if (element == "start_origin"):
            origin = self.start_event_origin
            action.drag_and_drop_by_offset(origin, horizontal_offset, vertical_offset).perform()

        elif (element == "task_origin"):
            origin = self.task_event_origin
            action.drag_and_drop_by_offset(origin, horizontal_offset, vertical_offset).perform()

        elif (element == "end_origin"):
            origin = self.end_event_origin
            action.drag_and_drop_by_offset(origin, horizontal_offset, vertical_offset).perform()

        else:
            origin = None

        # move element by x,y coordinates on the screen
        action.drag_and_drop_by_offset(origin, horizontal_offset, vertical_offset).perform()

    def connect_element(self, starting, ending):
        ''' Connects two elements. '''
        self.path_process_canvas()

        if (starting == "start"):
            self.start = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcessCanvas.START_EVENT_XPATH)))

        elif (starting == "task"):
            self.start = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcessCanvas.TASK_XPATH)))

        elif (starting == "end"):
            self.start = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcessCanvas.END_XPATH)))

        else:
            self.start = None

        ActionChains(self.driver).click(self.start).perform()

        self.flow = self.wait.until(EC.visibility_of_element_located((By.ID, PageProcessCanvas.FLOW_ID)))
        ActionChains(self.driver).click(self.flow).perform()

        if (ending == "start"):
            self.end = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcessCanvas.START_EVENT_XPATH)))

        elif (ending == "task"):
            self.end = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcessCanvas.TASK_XPATH)))

        elif (ending == "end"):
            self.end = self.wait.until(EC.visibility_of_element_located((By.XPATH, PageProcessCanvas.END_XPATH)))

        else:
            self.end = None

        ActionChains(self.driver).click(self.end).perform()

    def save_process(self):
        ''' Saves a process. '''
        self.path_process_canvas()

        self.save_button.click()
        self.commit_save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.COMMIT_SAVE_CSS)))
        self.commit_save.click()

        try:
            self.alert_save = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, PageProcessCanvas.SAVE_ALERT_CSS)))
            passed = True

        except AssertionError as e:
            passed = False
            raise Exception('Error while saving process', e)

        return passed
