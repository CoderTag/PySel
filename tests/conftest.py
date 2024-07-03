from selenium import webdriver
import pytest


#pytest hook to pass command line option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    # get browser from the command line
    browser_name = request.config.getoption("--browser_name")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.get("https://google.com")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
