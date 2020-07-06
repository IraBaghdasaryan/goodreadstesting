from Pages.base_page import BasePage
from Resource.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class FaildPage(BasePage):
    def __init__(self, driver):
        self.driver=driver
        self._visit("https://www.goodreads.com/")

    def failed_message_present(self):
        wait = WebDriverWait(self.driver,10)
        return wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#emailForm > div > div > span")))