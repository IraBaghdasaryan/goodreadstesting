from Pages.base_page import BasePage
from Resource.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FellowshipPage(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def add_to_read(self):
        self._click(Lotr_book_first.want_to_read)

    def mybook(self):
        self._click(HomePageLocators._mybooks)
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#books")))
