from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from test_data import Pages, LoginData
import random


class TestsRegistration:
    def test_registration_successful(self, driver):
        driver.get(Pages.registration_page_url)

        driver.find_element(*TestLocators.name_input_box).send_keys(LoginData.name)
        driver.find_element(*TestLocators.email_input_box).send_keys(str(random.randint(100,999)) + "@ya.ru")
        driver.find_element(*TestLocators.password_input_box).send_keys(str(random.randint(100000,999999)))
        driver.find_element(*TestLocators.sign_up_button).click()

        WebDriverWait(driver, 30).until(expected_conditions.url_changes(Pages.registration_page_url))

        assert driver.current_url == Pages.login_page_url

    def test_registration_invalid_password_validation_error_occurs(self, driver):
        driver.get(Pages.registration_page_url)

        driver.find_element(*TestLocators.name_input_box).send_keys(LoginData.name)
        driver.find_element(*TestLocators.email_input_box).send_keys(str(random.randint(100,999)) + "@ya.ru")
        driver.find_element(*TestLocators.password_input_box).send_keys(LoginData.short_password)
        driver.find_element(*TestLocators.sign_up_button).click()

        assert driver.find_element(*TestLocators.invalid_password_error)
