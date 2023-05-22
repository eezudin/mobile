from datetime import datetime

import pytest
import allure
import os
from helpers.application import Application
from appium.webdriver.appium_service import AppiumService
from helpers.config_reader import read_config


@pytest.fixture
def app(request):
    """starting and stopping the driver and passing the capability"""
    capabilities = read_config(request.config.getoption("--config"))
    fixture = Application(capabilities)

    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='session', autouse=True)
def appium_server(request):
    """starting and stopping appium server"""
    fixture = AppiumService()
    fixture.start()
    request.addfinalizer(fixture.stop)
    return fixture


# @pytest.fixture(scope="function")
# def allure_report(request):
#     allure_report_dir = "./allure-report"
#     allure_report_name = "allure_report"
#     allure.environment(report=report_dir)
#     yield
#     pytest.main(['--alluredir', allure_report_dir, request.node.name])
#     allure_report_cmd = f'allure generate {allure_report_dir} --clean -o {allure_report_name}'
#     os.system(allure_report_cmd)


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default='resources/configs/emulator.properties')

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        # execute all other hooks to obtain the report object
        outcome = yield
        rep = outcome.get_result()

        if rep.when == 'call' and rep.failed:
            file_name = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S_%F')}".replace("/", "_").replace("::", "__")
            capture_path = f"./screenshots/{file_name}.png"
            app.driver.save_screenshot(capture_path)
            allure.attach(
                app.driver.get_screenshot_as_png(), name=f'screenshot {file_name}',
                attachment_type=allure.attachment_type.PNG)
