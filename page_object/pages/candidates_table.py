from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.locators import Locator


class CandidatesTable:
    wait_time_out = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait_variable = WebDriverWait(self.driver, self.wait_time_out)

        # count of candidates
        self.count_of_candidates = 0

        # green button
        # self.green_button = driver.find_element(By.ID, Locator.green_button)

        # url
        self.desired_url = "https://rjovica-trials6518.orangehrmlive.com/client/#/noncore/recruitment/viewCandidates"

    def from_to_of(self):
        try:
            self.driver.switch_to.frame('noncoreIframe')
            WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(self.desired_url))
            assert self.desired_url in self.driver.current_url
            print('Candidates url is loaded')
            from_to_of_table = self.wait_variable.until(expected_conditions.presence_of_element_located((By.XPATH, Locator.from_to_of)))
            self.count_of_candidates = int(from_to_of_table.text.split(" of ")[1])
        except AssertionError:
            print('Candidates url is not loaded')

        return self.count_of_candidates
