from Pages.base_page import BasePage
from Resource.Locators import *


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def with_(self, username, password):
        self._type(LoginPageLocators._username_input, username)
        self._type(LoginPageLocators._password_input, password)
        self._click(LoginPageLocators._signin_button)


    def failure_message_present(self):
        return self._is_displayed(LoginPageLocators._login_failure)



