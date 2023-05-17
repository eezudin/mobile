import pytest
from helpers.application import Application
from appium.webdriver.appium_service import AppiumService


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


@pytest.fixture(scope='session', autouse=True)
def appium_server(request):
    fixture = AppiumService()
    fixture.start()
    request.addfinalizer(fixture.stop)
    return fixture
