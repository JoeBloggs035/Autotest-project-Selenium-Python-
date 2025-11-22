import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )

    parser.addoption(
        "--language",
        action="store",
        default="ru",
        help="Choose site language: es or fr or en-gb or ru or en-us",
    )


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    browser = None

    if browser_name == "chrome":
        print(f"\n\nstart chrome browser for test, language is {language}..")
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print(f"\n\nstart firefox browser for test, language is {language}..")
        options = FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
