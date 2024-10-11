import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    print(f"Opening {browser} driver")
    if browser == "chrome":
        myDriver = webdriver.Chrome()
    elif browser == "firefox":
        myDriver = webdriver.Firefox()
    yield myDriver
    myDriver.quit()

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute"
    )