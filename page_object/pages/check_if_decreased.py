from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class CheckIfDecreased:
    wait_time_out = 15

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        self.new_count_of_candidates = 0

    def after_delete_candidate(self):
        try:
            from_to_of_table = self.wait_variable.until(expected_conditions.presence_of_element_located((By.XPATH, Locator.from_to_of)))
            self.new_count_of_candidates = int(from_to_of_table.text.split(" of ")[1])
        except AssertionError:
            print('Candidates url is not loaded')
        except IndexError:
            print('list index out of range')

        return self.new_count_of_candidates

    def get_vacancies(self):
        vacancies = self.wait_variable.until(
            expected_conditions.presence_of_element_located((By.ID, Locator.vacancies)))

        return vacancies

    def get_candidates(self):
        candidates = self.wait_variable.until(
            expected_conditions.presence_of_element_located((By.ID, Locator.candidates_link)))

        return candidates
