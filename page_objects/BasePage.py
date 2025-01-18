from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def sendText(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        ).send_keys(text)
    
    def clickElement(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
    
    def isElementPresent(self, locator):
        try:
            elementToBeChecked = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return bool(elementToBeChecked)
        except:
            return False
    
    def getElementText(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        ).text
    
    def countOfElements(self, locator):
        try: 
            return len(WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
            ))
        except:
            return 0