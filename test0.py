from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep

class Testing(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://campusvirtualunillanos.co/")
		self.assertIn("Facebook", browser.title, msg="Titulos no coinciden")
		
	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()