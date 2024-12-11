from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from conftest import driver
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, locator, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_and_send_keys(self, locator, text, timeout=15):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def wait_element(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def enter_username(self, text):
        self.wait_and_send_keys(Locators.USERNAME_INPUT, text)

    def enter_password(self, text):
        self.wait_and_send_keys(Locators.PASSWORD_INPUT, text)

    def click_submit_button(self):
        self.wait_and_click(Locators.SUBMIT_BUTTON)

    def click_marketing_account(self):
        self.wait_and_click(Locators.ACCOUNTS_BUTTON)

    def click_create_marketing_account(self):
        self.wait_and_click(Locators.CREATE_ACCOUNT_BUTTON)

    def enter_name_account(self, text):
        self.wait_and_send_keys(Locators.NAME_INPUT, text)

    def enter_phone_account(self, text):
        self.wait_and_send_keys(Locators.PHONE_INPUT, text)

    def click_save_account_button(self):
        self.wait_and_click(Locators.SAVE_BUTTON)

    def click_marketing_leads(self):
        self.wait_and_click(Locators.OPEN_LEADS_BUTTON)

    def click_create_marketing_leads(self):
        self.wait_and_click(Locators.CREATE_LEADS_BUTTON)

    def enter_name_lead(self, text):
        self.wait_and_send_keys(Locators.NAME_LEADS_INPUT, text)

    def enter_lastname_lead(self, text):
        self.wait_and_send_keys(Locators.LASTNAME_LEADS_INPUT, text)

    def enter_phone_lead(self, text):
        self.wait_and_send_keys(Locators.PHONE_LEADS_INPUT, text)

    def click_account_name(self):
        self.wait_and_click(Locators.TAB_NAME_ACCOUNT)

    def click_add_lead_account(self):
        self.wait_and_click(Locators.OPEN_LEADS_BUTTON)

    def click_select_lead_button(self):
        self.wait_and_click(Locators.SELECT_CHANGE_CREATE)

    def click_select_add_lead_button(self):
        self.wait_and_click(Locators.SELECT_CHANGE_SELECT)

    def click_add_lead_to_account(self):
        self.wait_and_click(Locators.ADD_LEADS_BUTTON)






