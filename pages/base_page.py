from datetime import datetime

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))

    @allure.step('element')
    def tap(self, by_locator):
        self.get_element(by_locator).click()

    @allure.step('element')
    def type(self, by_locator, text):
        self.get_element(by_locator).send_keys(text)

    def check_element_text(self, by_locator, expected_text):
        # attach = self.driver.get_screenshot_as_png()
        # allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
        WebDriverWait(self.driver, 20).until(ec.text_to_be_present_in_element(by_locator, expected_text))



