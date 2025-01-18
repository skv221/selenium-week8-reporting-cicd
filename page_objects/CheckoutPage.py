from selenium.webdriver.common.by import By
from page_objects.ShoppingPage import ShoppingPage

class CheckoutPage(ShoppingPage):
    firstNameField = (By.NAME, "firstName")
    lastNameField = (By.NAME, "lastName")
    postalCodeField = (By.NAME, "postalCode")
    continueButton = (By.NAME, "continue")
    finishButton = (By.NAME, "finish")
    completeMessage = (By.CLASS_NAME, "complete-header")
    
    def formSubmit(self, firstName, lastName, postalCode):
        self.sendText(self.firstNameField, firstName)
        self.sendText(self.lastNameField, lastName)
        self.sendText(self.postalCodeField, postalCode)
        self.clickElement(self.continueButton)
    
    def validateForm(self):
        if self.isElementPresent(self.finishButton):
            return "Pass"
        elif self.isElementPresent(self.errorElement):
            return "Fail"
    
    def finishShopping(self):
        self.clickElement(self.finishButton)
    
    def validateShopping(self):
        if self.isElementPresent(self.completeMessage):
            return "Pass"
        else:
            return "Fail"