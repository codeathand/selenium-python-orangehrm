from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class Recruitment:
    wait_time_out = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # recruitment locators
        self.recruitment = driver.find_element(By.ID, Locator.recruitment_module)
        self.candidates = self.wait_variable.until(expected_conditions.presence_of_element_located((By.ID, Locator.candidates_link)))
        # self.candidates = driver.find_element(By.ID, Locator.candidatesLink)

    def get_recruitment(self):
        return self.recruitment

    def get_candidates(self):
        return self.candidates
