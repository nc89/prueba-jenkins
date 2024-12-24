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
        browser.get("https://www.w3schools.com/html/html_tables.asp")
        # Localizar filas de la tabla
        rows = browser.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
        extracted_data = []
    
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text for col in cols]
            if row_data:  # Evita filas vacías (como encabezados)
                extracted_data.append(row_data)
    
        # Verificar que se hayan extraído datos
        assert len(extracted_data) > 0
        print("Datos extraídos:", extracted_data)
        
    def tearDown(self):
       self.browser.quit()

if __name__ == '__main__':
	unittest.main()