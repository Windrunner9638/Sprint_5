from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from test_data import Pages, LoginData


class TestsLogout:
    def test_logout(self, driver):
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

        driver.find_element(*TestLocators.logout_button).click()
        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.profile_page_url))
        assert driver.current_url == Pages.login_page_url
