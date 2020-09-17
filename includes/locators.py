#!/usr/local/bin/python3

from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """ Class for Base Page locators. Navigation bar locators here. """
    REQUESTS_LINK = (By.LINK_TEXT, 'Requests')
    TASKS_LINK = (By.LINK_TEXT, 'Tasks')
    DESIGNER_LINK = (By.LINK_TEXT, 'Designer')
    ADMIN_LINK = (By.LINK_TEXT, 'Admin')
    AVATAR = (By.ID, 'avatarMenu')


class LoginPageLocators(object):
    """ Class for Login Page locators. All Login page locators here. """
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login')


class RequestsPageLocators(object):
    """ Class for Designer Page locators. All Designer page locators here. """
    MY_REQUESTS = (By.XPATH, "//i[@class='fas nav-icon fa-id-badge']")
    IN_PROGRESS = (By.XPATH, "//i[@class='fas nav-icon fa-clipboard-list']")
    COMPLETED = (By.XPATH, "//i[@class='fas nav-icon fa-clipboard-check']")
    ALL_REQUESTS = (By.XPATH, "//i[@class='fas nav-icon fa-clipboard']")


class AdminPageLocators(object):
    """ Class for Admin Page locators. All Admin page locators here. """
    USERS_TAB = (By.ID, 'nav-users-tab')
    DELETED_USERS_TAB = (By.ID, 'nav-deleted-users-tab')
    USERS_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-user']")
    GROUPS_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-users']")
    AUTH_CLIENTS_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-key']")
    CUSTOMIZE_UI_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-palette']")
    QUEUE_MANAGEMENT_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-infinity']")
    SCRIPT_EXECUTORS_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-code']")


class DesignerPageLocators(object):
    """ Class for Designer Page locators. All Designer page locators here. """
    PROCESSES_TAB = (By.ID, 'nav-sources-tab')
    CATEGORIES_TAB = (By.ID, 'nav-categories-tab')
    ARCHIVED_PROCESSES_TAB = (By.ID, 'nav-archived-tab')
    PROCESSES_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-play-circle']")
    SCRIPTS_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-code']")
    SCREENS_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-file-alt']")
    ENVIRONMENT_VARIABLES_BUTTON = (By.XPATH, "//i[@class='fas nav-icon fa-lock']")
