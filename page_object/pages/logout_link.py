from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class LogoutLink:
    wait_time_out = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # logout link
        # self.logout_link = self.wait_variable.until(
        #     expected_conditions.presence_of_element_located((By.ID, Locator.logout_link)))

    def get_logout_link(self):
        logout_link = self.wait_variable.until(
            expected_conditions.element_to_be_clickable((By.ID, Locator.logout_link)))
        return logout_link
