from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

class test_example(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_example(self):
        wd = self.wd
        self.open_page(wd, 'https://www.google.com/')
        self.clear_search_form(wd)
        self.fill_serch_form(wd, 'figujhblkfjgbnlfkj')

    def fill_serch_form(self, wd, Text):
        wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').send_keys(Text)

    def clear_search_form(self, wd):
        wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').clear()

    def open_page(self, wd, url):
        wd.get(url)

    def tearDown(self):
        self.wd.quit()



