from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class CheckBox:
    wait_time_out = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # check box
        self.check_box = self.wait_variable.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, Locator.check_box)))

    def get_checkbox(self):
        return self.check_box
