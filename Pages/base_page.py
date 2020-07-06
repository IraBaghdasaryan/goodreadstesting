from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage():
    def _init__(self, driver):
        self.driver = driver

    def _visit(self, url):
        self.driver.get(url)

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _is_displayed(self, locator):
        return self._find(locator).is_displayed()

    def _type(self, locator, inpute_test):
        self._find(locator).send_keys(inpute_test)

    def _find_element(self,locator, time=10):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))




