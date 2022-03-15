import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class prueba_selenium(unittest.TestCase):
    
    def setUp(self):        
        print("me ejecuto antes de cada test")
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor="http://selenoid:4444/wd/hub",
                           desired_capabilities={'browserName': 'chrome', 'browserVersion':'99.0', 'selenoid:options':{'enableVNC':True}})
        
    def test_a(self):        
        print("me ejecuto en cada test A")
        
        #GOOGLE
        self.driver.get("https://www.google.com")
        time.sleep(5)
        #aceptamos cookies
        self.driver.find_element(By.XPATH, "//div[text()='Acepto']/ancestor::button").click()
        time.sleep(5)
        #buscamos texto wikipedia                
        search_bar = self.driver.find_element(By.NAME, "q")
        time.sleep(5)
        search_bar.send_keys("wikipedia")
        time.sleep(5)
        search_bar.send_keys(Keys.ENTER)
        
        #BUSQUEDA DE GOOGLE
        self.driver.find_element(By.XPATH, "(//div[@id='search']/descendant::div[@class='g'])[1]/descendant::a[1]").click()
        
        #WIKIPEDIA
        title = self.driver.title
        
        self.assertEqual("Wikip la enciclopedia libre", title)
        pass
        
    def tearDown(self):
        print("me ejecuto después de cada test")
        self.driver.quit()
        pass
    

if __name__ == "__main__":
    unittest.main()
