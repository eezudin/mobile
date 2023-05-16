from appium import webdriver
from pages.start_page import StartPage
from pages.login_page import LoginPage
from pages.side_menu import SideMenu


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
        self.start_page = StartPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.side_menu = SideMenu(self.driver)

    def destroy(self):
        if self.driver:
            self.driver.quit()
