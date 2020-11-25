from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class OpenFormModal:
    wait_time_out = 5

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

    def get_green_button(self):
        green_button = self.driver.find_element(By.ID, Locator.green_button)
        return green_button

    def modal_header_is_visible(self):
        modal_header = self.wait_variable.until(expected_conditions.presence_of_element_located((By.XPATH, Locator.modal_header)))
        return modal_header
