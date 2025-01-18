from datetime import datetime
from keywords.keywords import openBrowser, navigateTo, killBrowser
from utilities.data_reader import read_json
from utilities.logger import logger
import pytest
import time

config = read_json("config\config.json")

browserType = config["browser"]["type"]
isHeadless = config["browser"]["headless"]
driverPath = config["driver_paths"]["chrome_driver"]

testURL = config["environment"]["base_url"]
waitTimw = config["browser"]["implicit_wait"]


@pytest.fixture
def setup_browser():
    driver = openBrowser(browserType, driverPath, isHeadless)
    navigateTo(driver, testURL, waitTimw)
    yield driver
    time.sleep(5)
    killBrowser(driver)

@pytest.fixture(scope="function")
def log():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    logFile = f"log/test_executed@{timestamp}.log"
    return logger(logFile)