from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from pages.common_methods import CommonMethods


class StartPage(CommonMethods, BasePage):

    """ Locators """
    popUpCloseButton = (AppiumBy.CLASS_NAME, 'android.widget.Button')
    skipTourButton = (AppiumBy.XPATH, "//*[@text = 'Skip Tour']")
    loginTitle = (AppiumBy.ID, 'com.rheem.contractor:id/tv_title')

    def close_popup(self):
        self.click(self.popUpCloseButton)

    def skip_tour(self):
        self.click(self.skipTourButton)

    def go_to_login_page(self):
        self.click(self.loginTitle)

    def check_user_logged(self, text):
        self.check_element_text(self.loginTitle, text)
