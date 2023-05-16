from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        self.get_element(by_locator).click()

    def send_keys(self, by_locator, text):
        self.get_element(by_locator).send_keys(text)

    def check_element_text(self, by_locator, expected_text):
        WebDriverWait(self.driver, 20).until(ec.text_to_be_present_in_element(by_locator, expected_text))



