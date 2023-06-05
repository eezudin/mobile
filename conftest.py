from datetime import datetime
import pytest
import allure
from helpers.application import Application
from appium.webdriver.appium_service import AppiumService
from helpers.config_reader import read_config


# @pytest.fixture(params=["device1", "device2"], scope="function")
@pytest.fixture(scope="function")
def app(request):
    """starting the driver and passing the capability"""

    capabilities = read_config(request.config.getoption("--config"))
    executor = request.config.getoption("--config")

    app = Application(executor, capabilities)
    yield app
    # request.addfinalizer(app.destroy)


# @pytest.fixture(scope='session', autouse=True)
# def appium_server(request):
#     """starting and stopping appium server"""
#
#     fixture = AppiumService()
#     fixture.start()
#     request.addfinalizer(fixture.stop)
#     return fixture


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default='resources/grid.properties')
    parser.addoption("--executor", action="store", default='192.168.0.19')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """set up a hook to be able to check if a test has failed"""

    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function", autouse=True)
def test_failed_check(request):
    yield

    driver = request.node.funcargs['app'].driver
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            take_screenshot(driver, request.node.nodeid)
            print("executing test failed", request.node.nodeid)
    driver.quit()


def take_screenshot(driver, node_id):
    file_name = f'{node_id}_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
    allure.attach(
        driver.get_screenshot_as_png(), name=f'screenshot {file_name}',
        attachment_type=allure.attachment_type.PNG)

# @pytest.fixture(scope="function")
# def allure_report(request):
#     allure_report_dir = "./allure-report"
#     allure_report_name = "allure_report"
#     allure.environment(report=report_dir)
#     yield
#     pytest.main(['--alluredir', allure_report_dir, request.node.name])
#     allure_report_cmd = f"allure generate {allure_report_dir} --clean -o {allure_report_name}"
#     os.system(allure_report_cmd)
