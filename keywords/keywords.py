from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.chrome.options import Options as chromeOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.firefox.options import Options as firefoxOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.edge.options import Options as edgeOptions
from utilities.data_reader import read_json

def openBrowser(browserType, driverPath, isHeadless):
    if browserType == 'chrome':
        if isHeadless:
            chrome_options = chromeOptions()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Chrome(service = chromeService(driverPath), options = chrome_options)
        else:
            return webdriver.Chrome(service = chromeService(driverPath))
    elif browserType == 'firefox':
        if isHeadless:
            firefox_options = firefoxOptions()
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--disable-gpu")
            firefox_options.add_argument("--window-size=1920,1080")
            firefox_options.add_argument("--no-sandbox")
            firefox_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Firefox(service = firefoxService(GeckoDriverManager().install()), options = firefox_options)
        else:     
            return webdriver.Firefox(service = firefoxService(GeckoDriverManager().install()))
    elif browserType == 'edge':
        if isHeadless:
            edge_options = edgeOptions()
            edge_options.add_argument("--headless")
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--window-size=1920,1080")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Edge(service = edgeService(EdgeChromiumDriverManager().install()), options = edge_options)
        else:
            return webdriver.Edge(service = edgeService(EdgeChromiumDriverManager().install()))
    elif browserType == 'cloud':
        browserStack = read_json("config\\browserstack_config.json")
        username = browserStack["browserstack"]["username"]
        access_key = browserStack["browserstack"]["access_key"]
        capabilities = browserStack["capabilities"]
        cloudBrowser = browserStack["capabilities"]["browser"]
        browserstack_url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"
        if cloudBrowser == 'Edge':
            edge_options = edgeOptions()
            for key, value in capabilities.items():
                edge_options.set_capability(key, value)
            if isHeadless:
                edge_options.add_argument("--headless")
                edge_options.add_argument("--disable-gpu")
                edge_options.add_argument("--window-size=1920,1080")
                edge_options.add_argument("--no-sandbox")
                edge_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Remote(command_executor = browserstack_url, options = edge_options)
        elif cloudBrowser == 'Chrome':
            chrome_options = chromeOptions()
            for key, value in capabilities.items():
                chrome_options.set_capability(key, value)
            if isHeadless:
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--window-size=1920,1080")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Remote(command_executor = browserstack_url, options = chrome_options)
        elif cloudBrowser == 'Firefox':
            firefox_options = firefoxOptions()
            for key, value in capabilities.items():
                firefox_options.set_capability(key, value)
            if isHeadless:
                firefox_options.add_argument("--headless")
                firefox_options.add_argument("--disable-gpu")
                firefox_options.add_argument("--window-size=1920,1080")
                firefox_options.add_argument("--no-sandbox")
                firefox_options.add_argument("--disable-dev-shm-usage")
            return webdriver.Remote(command_executor = browserstack_url, options = firefox_options)

        

def navigateTo(driver, url, waitTime):
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(waitTime)
    
def killBrowser(driver):
    driver.quit()
    
def xstr(s):
    return '' if s is None else str(s)

def buttonId(s):
    return s.lower().replace(" ","-")