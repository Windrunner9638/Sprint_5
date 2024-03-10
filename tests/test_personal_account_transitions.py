from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import Pages, LoginData
from selenium.webdriver.support import expected_conditions


class TestPersonalAccountTransitions:
    def test_transition_to_personal_account_when_login(self, driver):
        driver.get(Pages.base_url)
        driver.find_element(*TestLocators.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.base_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)

        driver.find_element(*TestLocators.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url

        driver.find_element(*TestLocators.personal_account_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located(TestLocators.logout_button))
        assert driver.current_url == Pages.profile_page_url

    def test_transition_from_personal_account_to_constructor_click_on_button(self, driver):
        driver.get(Pages.base_url)
        driver.find_element(*TestLocators.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.base_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)

        driver.find_element(*TestLocators.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url

        driver.find_element(*TestLocators.personal_account_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located(TestLocators.logout_button))
        assert driver.current_url == Pages.profile_page_url

        driver.find_element(*TestLocators.constructor_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.profile_page_url))
        assert driver.current_url == Pages.base_url

    def test_transition_from_personal_account_to_constructor_click_on_logo(self, driver):
        driver.get(Pages.base_url)
        driver.find_element(*TestLocators.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.base_url))
        assert driver.current_url == Pages.login_page_url

        driver.find_element(*TestLocators.email_input_box).send_keys(LoginData.email)
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.password)

        driver.find_element(*TestLocators.login_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.login_page_url))
        assert driver.current_url == Pages.base_url

        driver.find_element(*TestLocators.personal_account_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located(TestLocators.logout_button))
        assert driver.current_url == Pages.profile_page_url

        driver.find_element(*TestLocators.header_logo).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.profile_page_url))
        assert driver.current_url == Pages.base_url
