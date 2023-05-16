def test_successfully_login(app):
    app.start_page.close_popup()
    app.start_page.skip_tour()
    app.start_page.go_to_login_page()
    app.login_page.login('jeff.lebowski', 'Rheem789')
    app.start_page.check_user_logged('Hello, Jeff Lebowski!')


def test_successfully_login_2(app):
    app.start_page.close_popup()
    app.start_page.skip_tour()
    app.start_page.click_side_menu()
    app.side_menu.click_login()
    app.login_page.login('jeff.lebowski', 'Rheem789')
    app.start_page.check_user_logged('Hello, Jeff Lebowski!')


def test_failed_login(app):
    app.start_page.close_popup()
    app.start_page.skip_tour()
    app.start_page.go_to_login_page()
    app.login_page.login('jeff.lebowski', '789')
    app.login_page.check_toast_message('Invalid Username and/or Password')
