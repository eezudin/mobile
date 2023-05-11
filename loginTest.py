import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

capabilities = dict(
    platformName='Android',
    deviceName='emulator-5556',
    appPackage='com.rheem.contractor',
    app="C:\\Users\\ezudin\\PycharmProjects\\pythonProject\\resourses\\app-rheem-iat-release.apk",
    platformVersion="11.0",
    automationName='uiautomator2',
    appActivity='.MainActivity'
)

appium_server_url = 'http://localhost:4723'


class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_successfully_login(self) -> None:
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.Button")))
        button = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.Button')
        button.click()
        skip_tour = self.driver.find_element(by=AppiumBy.XPATH, value='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android.widget.TextView')
        skip_tour.click()
        WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((
            AppiumBy.ID, "com.rheem.contractor:id/tv_title")))
        go_to_login = self.driver.find_element(by=AppiumBy.ID, value='com.rheem.contractor:id/tv_title')
        go_to_login.click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located((
                AppiumBy.ID, "com.rheem.contractor:id/username_text_field")))
        login_field = self.driver.find_element(AppiumBy.ID, 'com.rheem.contractor:id/username_text_field')
        login_field.send_keys('jeff.lebowski')
        password_field = self.driver.find_element(AppiumBy.ID, 'com.rheem.contractor:id/password_text_field')
        password_field.send_keys('Rheem789')
        login_button = self.driver.find_element(AppiumBy.ID, 'com.rheem.contractor:id/login_button')
        login_button.click()
        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(
                (AppiumBy.ID, "com.rheem.contractor:id/tv_title")))
        WebDriverWait(self.driver, 20).until(
            expected_conditions.text_to_be_present_in_element((AppiumBy.ID, "com.rheem.contractor:id/tv_title"), 'Hello, Jeff Lebowski!'))


if __name__ == '__main__':
    unittest.main()
