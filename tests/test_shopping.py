from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class Testing(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def test_load(self):
		driver = self.browser
		driver.get("https://www.saucedemo.com/")
		# Login
		driver.find_element(By.ID, "user-name").send_keys("standard_user")
		driver.find_element(By.ID, "password").send_keys("secret_sauce")
		driver.find_element(By.ID, "login-button").click()

		# Agregar un producto al carrito
		driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
		driver.find_element(By.ID, "shopping_cart_container").click()
		time.sleep(2)
		# Verificar que el producto esté en el carrito
		assert "Sauce Labs Backpack" in driver.page_source

		# Checkout
		driver.find_element(By.ID, "checkout").click()
		driver.find_element(By.ID, "first-name").send_keys("John")
		driver.find_element(By.ID, "last-name").send_keys("Doe")
		driver.find_element(By.ID, "postal-code").send_keys("12345")
		driver.find_element(By.ID, "continue").click()
		driver.find_element(By.ID, "finish").click()
		time.sleep(2)
		assert "Thank you for your order!" in driver.page_source
  
	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()