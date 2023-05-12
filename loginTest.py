import pytest
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_successfully_login(app):
    app.close_popup()
    app.skip_tour()
    app.go_to_login_page()
    app.login('jeff.lebowski', 'Rheem789')
    app.check_user_logged()


def test_failed_login(app):
    app.close_popup()
    app.skip_tour()
    app.go_to_login_page()
    app.login('jeff.lebowski', '789')
    app.check_toast_message()
