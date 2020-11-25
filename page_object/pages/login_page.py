from selenium.webdriver.common.by import By

from page_object.locators import Locator


class Login:

    def __init__(self, driver):
        self.driver = driver

        # login page locators
        self.username = driver.find_element(By.ID, Locator.username)
        self.password = driver.find_element(By.ID, Locator.password)
        self.login_button = driver.find_element(By.ID, Locator.login_button)

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_login_button(self):
        return self.login_button
