import pytest
import allure
from locators.locators import Locators
from pages.base_page import BasePage
from src.config import BASE_URL, MAIN_URL
from src.data import TEST_DATA


@pytest.mark.usefixtures("driver")
class TestMainFunctionality:
    @allure.title("Успешная авторизация")
    def test_login(self, driver):
        driver.get(BASE_URL)
        page = BasePage(driver)
        page.enter_username(TEST_DATA["login"])
        page.enter_password(TEST_DATA["password"])
        page.click_submit_button()

        assert MAIN_URL in driver.current_url

    @allure.title("Создание контрагента")
    def test_create_account(self, driver):
        driver.get(BASE_URL)
        page = BasePage(driver)
        page.enter_username(TEST_DATA["login"])
        page.enter_password(TEST_DATA["password"])
        page.click_submit_button()
        page.click_marketing_account
        page.click_create_marketing_account
        page.enter_name_account("Tony")
        page.enter_phone_account("16460986510")
        page.click_save_account_button

        assert driver.find_element(*Locators.SUCCESS_NAME_ACCOUNT).is_displayed()

    @allure.title("Создание лида")
    def test_create_leads(self, driver):
        driver.get(BASE_URL)
        page = BasePage(driver)
        page.enter_username(TEST_DATA["login"])
        page.enter_password(TEST_DATA["password"])
        page.click_submit_button()
        page.click_marketing_account
        page.click_create_marketing_account
        page.enter_name_account("Tony")
        page.enter_phone_account("16460986510")
        page.click_save_account_button
        page.click_marketing_leads()
        page.click_create_marketing_leads()
        page.enter_name_lead("Rose")
        page.enter_lastname_lead("Minor")
        page.enter_phone_lead("79786785643")
        page.click_save_account_button()

        assert driver.find_element(*Locators.SUCCESS_NAME_LEADS).is_displayed()

    @allure.title("Прикрепление лида к контрагенту")
    def test_link_lead_account(self, driver):
        driver.get(BASE_URL)
        page = BasePage(driver)
        page.enter_username(TEST_DATA["login"])
        page.enter_password(TEST_DATA["password"])
        page.click_submit_button()
        page.click_marketing_account
        page.click_create_marketing_account
        page.enter_name_account("Tony")
        page.enter_phone_account("16460986510")
        page.click_save_account_button
        page.click_marketing_leads()
        page.click_create_marketing_leads()
        page.enter_name_lead("Rose")
        page.enter_lastname_lead("Minor")
        page.enter_phone_lead("79786785643")
        page.click_save_account_button()

        assert driver.find_element(*Locators.ADD_LEADS_BUTTON).is_displayed()
