from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage
from Resource.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def success_message_present(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"div.siteHeader__topLine.gr-box.gr-box--withShadow")))

    def search(self):
        self._click(HomePageLocators._search_button)

    def search_input(self, search):
        self._type(HomePageLocators._search_box, search)
        self._find(HomePageLocators._search_box).send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver,10)
        return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.content > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > h3")))


    def Menu(self):
        self._find(HomePageLocators._menu)

    #def mybooks(self):
        #self._click(HomePageLocators.want_to_read)




