# pytest -vs --tb=line --browser_name=chrome --language=en test_main_page.py
import time

from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(
        browser, link
    )  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page.open()  # открываем страницу
    # time.sleep(10)
    main_page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
    # 1-й способ - передача возвращаемого значения метода go_to_login_page() в переменную login_page
    # login_page = main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url) # 2-й способ - инициализация страницы в теле теста
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


"""
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
"""
