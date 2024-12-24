# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from time import sleep
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		browser = self.browser
		browser.get("https://campusvirtualunillanos.co/login/index.php")
		fname = browser.find_element(By.ID, 'username')
		fname.clear()
		fname.send_keys('Daniel')
		lname = browser.find_element(By.ID, 'password')
		lname.clear()
		lname.send_keys('Fernando')
		submitButton = browser.find_element(By.ID, 'loginbtn')
		submitButton.send_keys(Keys.ENTER)
		sleep(2)
		res = browser.find_element(By.CLASS_NAME, 'alert')
		self.assertEqual('Acceso inválido. Verificar credenciales.', res.text, msg="Fallido exitosamente")

	def tearDown(self):
		print()
		#self.browser.quit()

if __name__ == '__main__':
	unittest.main()