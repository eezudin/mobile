from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Application:

    def __init__(self):
        appium_server_url = 'http://localhost:4723'
        capabilities = dict(
            platformName='Android',
            deviceName='emulator-5556',
            appPackage='com.rheem.contractor',
            app="C:\\Users\\ezudin\\PycharmProjects\\pythonProject\\resourses\\app-rheem-iat-release.apk",
            platformVersion="11.0",
            automationName='uiautomator2',
            appActivity='.MainActivity'
        )

        self.driver = webdriver.Remote(appium_server_url, capabilities)
        self.driver.implicitly_wait(20)

    def check_user_logged(self):
        WebDriverWait(self.driver, 20).until(
            ec.text_to_be_present_in_element((AppiumBy.ID, "com.rheem.contractor:id/tv_title"),
                                             'Hello, Jeff Lebowski!'))

    def login(self, login, password):
        self.fill_login_field(login)
        self.fill_password_field(password)
        self.click_login_button()

    def click_login_button(self):
        login_button = self.driver.find_element(AppiumBy.ID, 'com.rheem.contractor:id/login_button')
        login_button.click()

    def fill_password_field(self, password):
        password_field = self.driver.find_element(AppiumBy.ID, 'com.rheem.contractor:id/password_text_field')
        password_field.send_keys(password)

    def fill_login_field(self, login):
        login_field = self.driver.find_element(AppiumBy.ID, 'com.rheem.contractor:id/username_text_field')
        login_field.send_keys(login)

    def go_to_login_page(self):
        go_to_login_button = self.driver.find_element(by=AppiumBy.ID, value='com.rheem.contractor:id/tv_title')
        go_to_login_button.click()

    def skip_tour(self):
        skip_tour_button = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text = 'Skip Tour']")
        skip_tour_button.click()

    def close_popup(self):
        button = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.Button')
        button.click()

    def destroy(self):
        if self.driver:
            self.driver.quit()

    def check_toast_message(self):
        toast = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.Toast')
        assert toast.text == 'Invalid Username and/or Password'
