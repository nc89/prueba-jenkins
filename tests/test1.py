from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from warnings import filterwarnings
filterwarnings("ignore")
import unittest


class Testing(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://campusvirtualunillanos.co/")
		list = browser.find_elements(By.CLASS_NAME, 'h-100')			
		self.assertIn("3114", list[1].find_element(By.TAG_NAME, 'h3').text, msg="Comparacion de cursos no valido")

	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()