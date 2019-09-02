# -*- coding: utf-8 -*-

import pytest
from model.user_generator import testdata

# testdata - it is a content generator for text fields in an object User
@pytest.mark.parametrize("user", testdata)
def test_registration(contrl, user):

    # Open login page
    contrl.open_login_page()

    # Go to registration page
    contrl.registration.go_to_reg_page()

    # Fill textarea company, name, surname, phone, email, password
    contrl.registration.fill_registration_textareas(user)

    # Click registration button
    contrl.registration.click_registration_button()

    # Checking that the email is already being used. If true = test skiped
    if (contrl.registration.check_waring_email_already_in_use(user) == True):
        pytest.skip("Skipped because email is already registered. Ignore it")
    else:
        pass

    # Check registration success messages
    assert True == contrl.registration.compare_registration_message()

    # Open login page
    contrl.open_login_page()

    # login
    contrl.session.login(user)

    # logout
    contrl.session.logout()

