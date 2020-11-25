from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class UserMenu:
    wait_time_out = 5

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # user menu
        self.user_menu = driver.find_element(By.ID, Locator.user_menu)

    def get_user_menu(self):
        return self.user_menu

    def wait_menu(self):
        logout_link = self.wait_variable.until(
            expected_conditions.presence_of_element_located((By.ID, Locator.logout_link)))
        return logout_link
