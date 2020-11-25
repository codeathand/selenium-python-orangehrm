class Locator:

    # login page locators
    username = "txtUsername"
    password = "txtPassword"
    login_button = "btnLogin"

    # recruitment
    recruitment_module = "menu_recruitment_viewRecruitmentModule"
    candidates_link = "menu_recruitment_viewCandidates"
    from_to_of = "//div[(@id='fromToOf')]/div"

    # open modal
    green_button = "list_item_add"
    modal_header = "//*[@id=\"modalAddCandidate\"]/div//h5[contains(text(), 'Add Candidate')]"

    # form modal
    add_resume = "addCandidate_resume"
    first_name = "addCandidate_firstName"
    last_name = "addCandidate_lastName"
    email = "addCandidate_email"
    vacancy_input = "//*[@id=\"add-candidate-vacancy-widget-container\"]"
    dropdown = "//div[@id='add-candidate-vacancy-widget-container']/div/ul/div/li/a/p[contains(text(), 'Software QA Engineer')]"
    dropdown_value = "textarea_addCandidate_vacancy"
    save_button = "saveCandidateButton"

    # check box
    check_box = "table.pagedata > tbody > tr:nth-child(1) > td > label"

    # three dots
    three_dots = "ohrmList_Menu"

    # delete link
    delete_link = "deleteItemBtn"

    # delete modal
    delete_modal = "modal-delete-candidate"

    # delete button
    delete_button = "candidate-delete-button"

    # user menu
    user_menu = "account-job"

    # logout link
    logout_link = "logoutLink"

    # vacancies
    vacancies = "menu_recruitment_viewJobVacancy"
