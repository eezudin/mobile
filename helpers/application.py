from appium import webdriver
from pages.start_page import StartPage
from pages.login_page import LoginPage
from pages.side_menu import SideMenu


class Application:

    def __init__(self, executor,  capabilities):
        self.capabilities = capabilities
        self.executor = executor

        # appium_server_url = 'http://localhost:4723'
        appium_server_url = f'http://{executor}:4444/wd/hub'
        self.driver = webdriver.Remote(appium_server_url, self.capabilities)
        self.driver.implicitly_wait(20)
        self.start_page = StartPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.side_menu = SideMenu(self.driver)

    def destroy(self):
        if self.driver:
            self.driver.quit()
