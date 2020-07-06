from Pages.base_page import BasePage
from Resource.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def choose_book(self):
        self._click(Search_LOTR._lotr1)
        #wait = WebDriverWait(self.driver, 10)
        #return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#topcol")))

