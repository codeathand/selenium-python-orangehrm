from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class AddCandidate:
    wait_time_out = 40

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # form modal locators
        # self.add_resume = driver.find_element(By.ID, Locator.add_resume)
        # self.first_name = driver.find_element(By.ID, Locator.first_name)
        # self.last_name = driver.find_element(By.ID, Locator.last_name)
        # self.email = driver.find_element(By.ID, Locator.email)
        # self.vacancy_input = driver.find_element(By.XPATH, Locator.vacancy_input)
        # self.dropdown = driver.find_element(By.XPATH, Locator.dropdown)
        # self.dropdown_value = driver.find_element(By.ID, Locator.dropdown_value)
        # self.save_button = driver.find_element(By.ID, Locator.save_button)

    def select_resume(self):
        add_resume = self.driver.find_element(By.ID, Locator.add_resume)
        return add_resume

    def get_firstname(self):
        first_name = self.wait_variable.until(expected_conditions.element_to_be_clickable((By.ID, Locator.first_name)))
        return first_name

    def get_lastname(self):
        last_name = self.driver.find_element(By.ID, Locator.last_name)
        return last_name

    def get_email(self):
        email = self.driver.find_element(By.ID, Locator.email)
        return email

    def get_vacancy_input(self):
        vacancy_input = self.driver.find_element(By.XPATH, Locator.vacancy_input)
        return vacancy_input

    def dropdown(self):
        dropdown = self.driver.find_element(By.XPATH, Locator.dropdown)
        return dropdown

    def dropdown_value(self):
        dropdown_value = self.driver.find_element(By.ID, Locator.dropdown_value)
        return dropdown_value

    def save_button(self):
        save_button = self.driver.find_element(By.ID, Locator.save_button)
        return save_button

    def form_is_closed(self):
        modal = self.wait_variable.until(expected_conditions.invisibility_of_element_located((By.XPATH, Locator.modal_header)))
        return modal
