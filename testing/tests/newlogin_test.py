from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.login_failed_page import FaildPage
import pytest

#Check login functionality
#Check system behavior when valid email and password is entered.

class Test_Login():
    def test_valid_login(self, browser):
        login_pg = LoginPage(browser)
        home_pg = HomePage(browser)
        browser.get("https://www.goodreads.com/")
        login_pg.with_("irairina27@gmail.com", "SuperPassword")
        assert home_pg.success_message_present()
        print("successful login")


#Check system behavior when 1. invalid email and password is entered, 2. valid email invalid password, 3 invalid email, valid password
#I used parametrize testing for invalid login test
    @pytest.mark.parametrize("username, password", [
        ("irina@gmail.com","ertyuv"),
        ("ira@gmail.com", "gfg123"),
        ("irairina27@gmail.com", "1234")
    ])
    def test_wrong_pass(self, username, password, browser):
        browser.get("https://www.goodreads.com/")
        login_pg = LoginPage(browser)
        fail_pg = FaildPage(browser)
        login_pg.with_(username, password)
        assert fail_pg.failed_message_present()