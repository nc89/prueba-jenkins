# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.common.by import By

class Testing(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_load(self):
        browser = self.browser
        browser.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")
        # Cambiar al iframe que contiene el formulario
        browser.switch_to.frame("iframeResult")
        # Completar el formulario
        browser.find_element(By.NAME, "fname").send_keys("John")
        browser.find_element(By.NAME, "lname").send_keys("Doe")
        browser.find_element(By.XPATH, "//input[@type='submit']").click()

        time.sleep(2)
        # Verificar el resultado
        assert "Your input was received" in browser.page_source
        
    def tearDown(self):
       self.browser.quit()

if __name__ == '__main__':
	unittest.main()