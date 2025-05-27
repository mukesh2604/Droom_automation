from datetime import datetime
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome or edge or firefox")

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser").lower()

    if browser == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        # from webdriver_manager.chrome import ChromeDriverManager
        # from selenium import webdriver
        #
        # driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=0).install())

        driver = webdriver.Chrome(service=service)
        print("lanching chrome browser")
    elif browser == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
        print("lanching edge browser")
    elif browser == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        print("launching firefox browser")
    else:
        raise Exception(f"Browser '{browser}' is not supported. Choose from: chrome, edge, firefox.")

    driver.maximize_window()
    yield driver  # Pass driver to the test

    # print("Closing the browser")
    # driver.quit()  # Clean up after test

####### pyest html report #####

def pytest_configure(config):
    config.metadata['project name'] = 'droom'
    config.metadata['module_name'] = 'sanity'
    config.metadata['Droom_Tech'] = 'Droom Qa Team'

###  it is hook for delete/modify env info to html report
@pytest.mark.opionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)


########## specifying report folder location and save location with timestamp.
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"