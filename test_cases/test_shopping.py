from page_objects.CheckoutPage import CheckoutPage
from utilities.data_reader import read_json, read_excel
from keywords.keywords import xstr
from time import sleep
import pytest
import allure

config = read_json("config/config.json")

browserType = config["browser"]["type"]
testDataPath = config["test_data"]["file_path"]
testDataSheet = config["test_data"]["TC_2_sheet_name"]

sleepTime = config["browser"]["sleep_time"]

def getTestData():
    return read_excel(testDataPath, testDataSheet)

@allure.feature("Shopping functionality")
@allure.story("Shopping in the site with valid and invalid operations")    
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("tc_id, name, password, expected, addItems, removeItems, firstName, lastName, PostalCode, ExpectedAction", getTestData())
def test_shopping(setup_browser, log, tc_id, name, password, expected, addItems, removeItems, firstName, lastName, PostalCode, ExpectedAction):
    log.info("Executing "+ tc_id + " with " + xstr(name) + " as username and " + xstr(password) + " as password in "+ browserType +" browser..." )
    
    with allure.step("Step 1: Open the browser and navigate to required site"):
        driver = setup_browser
        log.info("Starting browser session...")
    
    with allure.step("Step 2: Enter the login credentials from test data"):
        shopping = CheckoutPage(driver)
        log.info("Entering login credentials...")
        allure.attach(f"Username: {xstr(name)}", name="Username", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Password: {xstr(password)}", name="Password", attachment_type=allure.attachment_type.TEXT)
        shopping.login(xstr(name), xstr(password))
        sleep(sleepTime)
    
    with allure.step("Step 3: Validate the login and capture error message incase of invalid credentials"):    
        log.info("Validating login...")
        result = shopping.validatelogin()
        if result == "Pass":
            log.info("Logged in successfully")
        else:
            log.error(shopping.getErrorText())
        log.info("Login Check performed successfully...")
    
    with allure.step("Step 4: Add items to the cart in case of successful login"):
        try:
            assert expected == result
            if result == "Pass":
                log.info("Adding required items to cart..")
                itemsToAdd = xstr(addItems).split(", ")
                itemsToRemove = xstr(removeItems).split(", ")
                totalItems = len(itemsToAdd) - len(itemsToRemove)
                for item in itemsToAdd:
                    sleep(sleepTime)
                    log.info("Adding "+ item +" to cart..")
                    shopping.addItem(item)
                with allure.step("Step 5: Proceed to the cart and remove items as per test data"):
                    log.info("Proceeding to cart..")
                    shopping.proceedToCart()
                    for item in itemsToRemove:
                        sleep(sleepTime)
                        log.info("Removing "+ item +" from cart..")
                        shopping.removeItem(item)
                with allure.step("Step 6: Verify if correct items are present in the cart"):
                    log.info("Checking if all the required items are added and removed as expected...")
                    if not shopping.validateCartItems(totalItems):
                        log.error("Items in the cart doesn't match the expected items")
                        raise AssertionError("The shopping items do not match the expected list...")
                with allure.step("Step 7: Proceed to checkout and enter the required details"):
                    shopping.proceedToCheckout()
                    log.info("Proceeding to checkout..")
                    log.info("Entering form details..")
                    sleep(sleepTime)
                    shopping.formSubmit(xstr(firstName), xstr(lastName), xstr(PostalCode))
                with allure.step("Step 8: Verify if the form details are valid"):
                    formResult = shopping.validateForm()
                    if formResult == "Pass":
                        log.info("Completing the transaction...")
                    else:
                        log.error(shopping.getErrorText())
                    try:
                        assert ExpectedAction == formResult
                        with allure.step("Step 9: Proceed to transaction page and finish shopping"):
                            if formResult == "Pass":
                                sleep(sleepTime)
                                shopping.finishShopping()
                                with allure.step("Step 10: Verify if the shopping is completed"):    
                                    sleep(sleepTime)
                                    shoppingResult = shopping.validateShopping()
                                    if shoppingResult == "Pass":
                                        log.info("Shopping completed successfully...")
                                    else:
                                        log.error("Shopping is terminated...")
                                        raise AssertionError("The expected outcome was not achieved")
                    except Exception as e:
                        log.error("The process did not complete as expected..."+ str(e))
                        pytest.fail(str(e))    
        except Exception as e:
            log.error("An error was encountered during the process..."+ str(e))
            pytest.fail(str(e))
        finally:
            log.info("Quitting the browser session...")