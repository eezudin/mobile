from appium import webdriver


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

    def destroy(self):
        if self.driver:
            self.driver.quit()
