from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class LoginPage(BasePage):

    """ Locators """
    loginButton = (AppiumBy.ID, 'com.rheem.contractor:id/login_button')
    loginField = (AppiumBy.ID, 'com.rheem.contractor:id/username_text_field')
    passwordField = (AppiumBy.ID, 'com.rheem.contractor:id/password_text_field')
    toastMessage = (AppiumBy.XPATH, '/hierarchy/android.widget.Toast')

    def login(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.click_login_button()

    def click_login_button(self):
        self.click(self.loginButton)

    def fill_password_field(self, password):
        self.send_keys(self.passwordField, password)

    def fill_login_field(self, login):
        self.send_keys(self.loginField, login)

    def check_toast_message(self, expected_text):
        self.check_element_text(self.toastMessage, expected_text)
