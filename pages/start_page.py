import allure
from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.common_methods import CommonMethods


class StartPage(CommonMethods, BasePage):

    """ Locators """
    popUpCloseButton = (AppiumBy.CLASS_NAME, 'android.widget.Button')
    skipTourButton = (AppiumBy.XPATH, "//*[@text = 'Skip Tour']")
    loginTitle = (AppiumBy.ID, 'com.rheem.contractor:id/tv_title')

    @allure.step('Close popup window')
    def close_popup(self):
        self.tap(self.popUpCloseButton)

    @allure.step('Tap "Skip Tour" button')
    def skip_tour(self):
        self.tap(self.skipTourButton)

    @allure.step('Tap "Log In"')
    def go_to_login_page(self):
        self.tap(self.loginTitle)

    @allure.step('Check the name of the user in the greeting text')
    def check_user_logged(self, expected_text):
        self.check_element_text(self.loginTitle, f"Hello, {expected_text}!")
