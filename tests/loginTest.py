import allure
import pytest
from resources.settings import username, password, display_name
from helpers.constants import INVALID_LOGIN_MESSAGE


@allure.story('I wanna log In!!!')
@allure.feature('Not so good feature')
@allure.severity('blocker')
@allure.title('Log in: Main Screen')
def test_successfully_login(app):
    """Try to log in with correct user from main screen"""

    app.start_page.close_popup()
    app.start_page.skip_tour()
    app.start_page.go_to_login_page()
    app.login_page.login(username, password)
    app.start_page.check_user_logged(display_name)


@allure.story('I wanna log In!!!')
@allure.feature('Best feature ever')
@allure.severity('critical')
@pytest.mark.skip('[ISSUE-12345] Broken connection')
@allure.title('Log in: Side Menu')
def test_successfully_login_2(app):
    """Try to log in with correct user from side menu"""

    app.start_page.close_popup()
    app.start_page.skip_tour()
    app.start_page.click_side_menu()
    app.side_menu.click_login()
    app.login_page.login(username, password)
    app.start_page.check_user_logged(display_name)


@allure.story('I wanna log In!!!')
@allure.feature('It`s not a bug, it`s feature')
@allure.severity('trivial')
@allure.title('Log in: Main Screen Incorrect password')
def test_failed_login(app):
    """Try to log in with incorrect password"""

    app.start_page.close_popup()
    app.start_page.skip_tour()
    app.start_page.go_to_login_page()
    app.login_page.login(username, '789')
    app.login_page.check_toast_message(INVALID_LOGIN_MESSAGE)
