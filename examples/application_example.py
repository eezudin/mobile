# from selenium.webdriver.firefox.webdriver import WebDriver
# from selenium.webdriver.common.by import By
#
#
# class Application:
#     def __init__(self):
#         self.wd = WebDriver()
#         self.wd.implicitly_wait(60)
#
#     def fill_search_form(self, text):
#         wd = self.wd
#         wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').send_keys(text)
#
#     def clear_search_form(self):
#         wd = self.wd
#         wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').clear()
#
#     def open_page(self, url):
#         wd = self.wd
#         wd.get(url)
#
#     def destroy(self):
#         self.wd.quit()
