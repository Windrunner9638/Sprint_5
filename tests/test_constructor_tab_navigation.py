from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from test_data import Pages
from selenium.webdriver.support import expected_conditions


class TestConstructorTabNavigation:

    def test_constructor_transition_to_sauces_tab(self, driver):
        driver.get(Pages.base_url)
        driver.find_element(*TestLocators.sauces_tab).click()
        assert WebDriverWait(driver, 30).until(
            expected_conditions.text_to_be_present_in_element_attribute(TestLocators.sauces_tab, 'class', 'current'))

    def test_constructor_transition_to_toppings_tab(self, driver):
        driver.get(Pages.base_url)
        driver.find_element(*TestLocators.toppings_tab).click()
        assert WebDriverWait(driver, 30).until(
            expected_conditions.text_to_be_present_in_element_attribute(TestLocators.toppings_tab, 'class', 'current'))

    def test_constructor_transition_to_buns_tab(self, driver):
        driver.get(Pages.base_url)

        driver.find_element(*TestLocators.toppings_tab).click()
        WebDriverWait(driver, 30).until(
            expected_conditions.text_to_be_present_in_element_attribute(TestLocators.toppings_tab, 'class', 'current'))

        driver.find_element(*TestLocators.buns_tab).click()

        assert WebDriverWait(driver, 30).until(
            expected_conditions.text_to_be_present_in_element_attribute(TestLocators.buns_tab, 'class', 'current'))