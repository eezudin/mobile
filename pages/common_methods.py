from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CommonMethods(BasePage):

    """ Locators """
    sideMenuButton = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')

    def click_side_menu(self):
        self.click(self.sideMenuButton)
