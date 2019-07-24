import unittest
from selenium import webdriver


class FirstTest(unittest.TestCase):
    def test_first_selenium_test(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8000")
        self.driver.quit()
