import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#options = Options()
#options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#browser = webdriver.Chrome(options=options)

def pytest_addoption(parser):
   parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
   parser.addoption('--language', action='store', default=None,
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
   user_language = request.config.getoption("language")
   browser_name = request.config.getoption("browser_name")
   browser = None
   print("\nstart chrome browser for test..")
   browser = webdriver.Chrome()
   yield browser
   print("\nquit browser..")
   browser.quit()
