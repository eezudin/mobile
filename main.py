from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

class test_example(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def test_example(self):
        success = True
        wd = self.wd
        wd.get('https://www.google.com/')
        wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').click()
        wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').clear()
        wd.find_element(By.CSS_SELECTOR, 'textarea[type="search"]').send_keys('jldfhlvdhfl')
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()



