from Pages.base_page import BasePage
from Resource.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MybookPage(BasePage):
    def __init__(self, driver):
        self.driver=driver

    def book_on_shelf(self):
        self._find(myShelves._Lotr_first)
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#rightCol")))

    def delete(self):
        self._click(myShelves._delete_book)

    def verify_empty_shelf(self):
        self._find(myShelves._empty_shelf)
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.greyText.nocontent.stacked")))




