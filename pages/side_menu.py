from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class SideMenu(BasePage):
    """ Locators """
    logIn = (AppiumBy.ID, "com.rheem.contractor:id/account_settings_text_view")

    def click_login(self):
        self.click(self.logIn)
