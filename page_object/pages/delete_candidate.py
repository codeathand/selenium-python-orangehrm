from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class DeleteCandidate:
    wait_time_out = 250

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # delete link
        # self.delete_link = self.wait_variable.until(
        #     expected_conditions.element_to_be_clickable((By.ID, Locator.delete_link)))
        # self.delete_modal = self.wait_variable.until(
        #     expected_conditions.visibility_of_element_located((By.ID, Locator.delete_modal)))
        # self.delete_button = self.wait_variable.until(
        #     expected_conditions.presence_of_element_located((By.ID, Locator.delete_button)))

    def get_menu_delete_link(self):
        delete_link = self.wait_variable.until(
            expected_conditions.element_to_be_clickable((By.ID, Locator.delete_link)))
        return delete_link

    def delete_modal_is_displayed(self):
        delete_modal = self.wait_variable.until(
            expected_conditions.visibility_of_element_located((By.ID, Locator.delete_modal)))
        return delete_modal

    def get_delete_button(self):
        delete_button = self.wait_variable.until(
            expected_conditions.presence_of_element_located((By.ID, Locator.delete_button)))
        return delete_button

    def delete_modal_is_not_displayed(self):
        delete_modal = self.wait_variable.until(
            expected_conditions.invisibility_of_element_located((By.ID, Locator.delete_modal)))
        return delete_modal
