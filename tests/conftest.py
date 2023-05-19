import pytest
from helpers.application import Application
from appium.webdriver.appium_service import AppiumService
from helpers.config_reader import read_config


@pytest.fixture
def app(request):
    capabilities = read_config(request.config.getoption("--config"))
    fixture = Application(capabilities)
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='session', autouse=True)
def appium_server(request):
    fixture = AppiumService()
    fixture.start()
    request.addfinalizer(fixture.stop)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default='../resources/configs/emulator.properties')
