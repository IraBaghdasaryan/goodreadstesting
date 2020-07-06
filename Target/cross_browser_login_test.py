from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from Pages.home_page import HomePage
from Pages.login_page import LoginPage

class Test_Login():
    chrome = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
    firefox = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.FIREFOX)

    login_pg = LoginPage(chrome)
    home_pg = HomePage(chrome)
    chrome.get("https://www.goodreads.com/")
    login_pg.with_("irairina27@gmail.com", "SuperPassword")
    assert home_pg.success_message_present()
    print("successful login with chrome")


    firefox.get("https://www.goodreads.com/")
    login_pg = LoginPage(firefox)
    home_pg = HomePage(firefox)
    login_pg.with_("irairina27@gmail.com", "SuperPassword")
    assert home_pg.success_message_present()
    print("successful login with firefox")

    chrome.quit()
    firefox.quit()



