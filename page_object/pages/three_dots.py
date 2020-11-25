from selenium.webdriver.common.by import By

from page_object.locators import Locator


class ThreeDots:

    def __init__(self, driver):
        self.driver = driver

        # three dots
        self.three_dots_button = driver.find_element(By.ID, Locator.three_dots)

    def get_three_dots_button(self):
        return self.three_dots_button
