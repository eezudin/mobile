import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CommonMethods(BasePage):

    """ Locators """
    sideMenuButton = (AppiumBy.CLASS_NAME, 'android.widget.ImageButton')

    @allure.step('Tap Side Menu')
    def click_side_menu(self):
        self.tap(self.sideMenuButton)
