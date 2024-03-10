from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from test_data import Pages, LoginData


class TestsLogin:
    def test_successful_login_main_page_enter_account_button(self, driver):
        driver.get(Pages.base_url)

        driver.find_element(*TestLocators.login_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.base_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)
        driver.find_element(*TestLocators.login_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url

    def test_successful_login_main_page_personal_account(self, driver):
        driver.get(Pages.base_url)

        driver.find_element(*TestLocators.personal_account_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.base_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)
        driver.find_element(*TestLocators.login_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url

    def test_successful_login_registration_page_button(self, driver):
        driver.get(Pages.registration_page_url)
        driver.find_element(*TestLocators.login_link).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.registration_page_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)
        driver.find_element(*TestLocators.login_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url

    def test_successful_forgot_password_page_button(self, driver):
        driver.get(Pages.forgot_password_page_url)
        driver.find_element(*TestLocators.login_link).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.forgot_password_page_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)
        driver.find_element(*TestLocators.login_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url
