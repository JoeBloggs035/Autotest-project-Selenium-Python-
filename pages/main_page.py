from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # 1-й способ реализации перехода между страницами: возвращать нужный Page Obgect
        # return LoginPage(browser=self.browser, url=self.browser.current_url)
        # 2-й способ без return

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK
        ), "Login link is not presented"
