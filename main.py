from application import Application
import unittest

class test_example(unittest.TestCase):
    def setUp(self):
        self.app = Application()


    def test_example(self):
        self.app.open_page('https://www.google.com/')
        self.app.clear_search_form()
        self.app.fill_search_form('figujhblkfjgbnlfkj')

    def tearDown(self):
        self.app.destroy()



