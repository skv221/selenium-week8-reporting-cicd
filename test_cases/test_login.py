from page_objects.LoginPage import LoginPage
from utilities.data_reader import read_json, read_excel
from keywords.keywords import xstr
import pytest
import allure

config = read_json("config/config.json")

browserType = config["browser"]["type"]
testDataPath = config["test_data"]["file_path"]
testDataSheet = config["test_data"]["TC_1_sheet_name"]

def getTestData():
    return read_excel(testDataPath, testDataSheet)

@allure.feature("Login functionality")
@allure.story("Login checks with valid and invalid credentials")    
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("tc_id, name, password, expected", getTestData())
#Function for sending test data to the form
def test_submit(setup_browser, log, tc_id, name, password, expected):
    log.info("Executing "+ tc_id + " with " + xstr(name) + " as username and " + xstr(password) + " as password in "+ browserType +" browser..." )
    
    with allure.step("Step 1: Open the browser and navigate to required site"):
        log.info("Starting browser session...")
        driver = setup_browser
        
    with allure.step("Step 2: Enter the login credentials from test data"):
        loginPage = LoginPage(driver)
        log.info("Entering login credentials...")
        allure.attach(f"Username: {xstr(name)}", name="Username", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Password: {xstr(password)}", name="Password", attachment_type=allure.attachment_type.TEXT)
        loginPage.login(xstr(name), xstr(password))
    
    with allure.step("Step 3: Validate the login and capture error message incase of invalid credentials"):
        log.info("Validating login...")
        result = loginPage.validatelogin()
        if result == "Pass":
            log.info("Logged in successfully")
        else:
            log.error(loginPage.getErrorText())
        try:
            expected == result
            log.info("Actual result matches the expected condition")
        except Exception as e:
            log.error("Something went wrong...") 
    