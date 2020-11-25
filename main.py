import os

from selenium import webdriver

from page_object.pages.login_page import Login
from page_object.pages.recruitment import Recruitment
from page_object.pages.candidates_table import CandidatesTable
from page_object.pages.open_form_modal import OpenFormModal
from page_object.pages.add_candidate import AddCandidate
from page_object.pages.check_if_increased import CheckIfIncreased
from page_object.pages.check_if_decreased import CheckIfDecreased
from page_object.pages.check_box import CheckBox
from page_object.pages.three_dots import ThreeDots
from page_object.pages.delete_candidate import DeleteCandidate
from page_object.pages.user_menu import UserMenu
from page_object.pages.logout_link import LogoutLink

PATH = os.getcwd() + '\\drivers\\geckodriver-v0.28.0-win64\\geckodriver.exe'
driver = webdriver.Firefox(executable_path=PATH)
base_url = "https://rjovica-trials6518.orangehrmlive.com/"
path = os.getcwd() + '\\screenshots'
access_rights = 0o755
option = 'Software QA Engineer'

candidates_table = CandidatesTable(driver)
open_form_modal = OpenFormModal(driver)
add_candidate = AddCandidate(driver)
check_if_increased = CheckIfIncreased(driver)
check_if_decreased = CheckIfDecreased(driver)
delete_candidate = DeleteCandidate(driver)
logout_link = LogoutLink(driver)


def setup():
    driver.get(base_url)
    driver.maximize_window()


def login_page():
    login = Login(driver)
    login.get_username().send_keys('Admin')
    login.get_password().send_keys('MyspUNX9@5')
    try:
        os.mkdir(path, access_rights)
    except FileExistsError:
        print('Directory exists: ' + str(os.path.exists(path)))
    except OSError:
        print('Creation of directory %s failed: ' % path)

    driver.save_screenshot(f'{path}/before_click.png')
    login.get_login_button().click()


def recruitment_menu():
    recruitment = Recruitment(driver)
    recruitment.get_recruitment().click()
    recruitment.get_candidates().click()


def candidates_table_from_to_of():
    candidates_table.from_to_of()
    # print(candidates_table.count_of_candidates)


def open_add_candidate_form():
    open_form_modal.get_green_button().click()
    open_form_modal.modal_header_is_visible()


# def wait_for_modal():
#     open_form_modal.modal_header_is_visible()


def fill_add_candidate_form():
    driver.implicitly_wait(5)
    add_candidate.get_firstname().send_keys('QA')
    add_candidate.get_lastname().send_keys('Automation')
    add_candidate.get_email().send_keys('qa@qa.com')
    add_candidate.select_resume().send_keys(f'{os.getcwd()}\\Jovica_Raicki_CV_english.pdf')
    add_candidate.get_vacancy_input().click()
    add_candidate.dropdown().click()
    assert add_candidate.dropdown_value().text == option
    add_candidate.save_button().click()
    add_candidate.form_is_closed()


def check_if_number_of_candidates_increased():
    check_if_increased.after_adding_new_candidate()
    print(candidates_table.count_of_candidates)
    print(check_if_increased.new_count_of_candidates)
    try:
        assert candidates_table.count_of_candidates == check_if_increased.new_count_of_candidates - 1
    except AssertionError:
        print('assertion error')


def select_candidate():
    check_box = CheckBox(driver)
    check_box.get_checkbox().click()


def click_on_three_dots_menu():
    three_dots = ThreeDots(driver)
    three_dots.get_three_dots_button().click()


def delete_selected_candidate():
    delete_candidate.get_menu_delete_link().click()
    delete_candidate.delete_modal_is_displayed()
    delete_candidate.get_delete_button().click()
    delete_candidate.delete_modal_is_not_displayed()


def check_if_number_of_candidates_decreased():
    check_if_decreased.get_vacancies().click()
    check_if_decreased.get_candidates().click()
    check_if_decreased.after_delete_candidate()
    print(candidates_table.count_of_candidates)
    print(check_if_decreased.new_count_of_candidates)
    try:
        assert candidates_table.count_of_candidates == check_if_decreased.new_count_of_candidates
    except AssertionError:
        print('assertion error')


def open_user_menu():
    user_menu = UserMenu(driver)
    user_menu.get_user_menu().click()
    user_menu.wait_menu()


def click_logout_link():
    logout_link.get_logout_link().click()


setup()
login_page()
recruitment_menu()
candidates_table_from_to_of()
open_add_candidate_form()
fill_add_candidate_form()
check_if_number_of_candidates_increased()
select_candidate()
click_on_three_dots_menu()
delete_selected_candidate()
check_if_number_of_candidates_decreased()
open_user_menu()
click_logout_link()
