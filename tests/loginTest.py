from pages.start_page import StartPage
from pages.login_page import LoginPage


def test_successfully_login(app):
    start_page = StartPage(app.driver)
    login_page = LoginPage(app.driver)

    start_page.close_popup()
    start_page.skip_tour()
    start_page.go_to_login_page()
    login_page.login('jeff.lebowski', 'Rheem789')
    start_page.check_user_logged('Hello, Jeff Lebowski!')


def test_failed_login(app):
    start_page = StartPage(app.driver)
    login_page = LoginPage(app.driver)

    start_page.close_popup()
    start_page.skip_tour()
    start_page.go_to_login_page()
    login_page.login('jeff.lebowski', '789')
    login_page.check_toast_message('Invalid Username and/or Password')
