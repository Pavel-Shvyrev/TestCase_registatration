# -*- coding: utf-8 -*-

import pytest

from model.user_generator import testdata


# testdata - it is a content generator for text fields in an object User
@pytest.mark.parametrize("user", testdata)
def test_registration(controller, user):

    controller.open_login_page()

    controller.session.go_to_reg_page()

    controller.registration.fill_registration_text_areas(user)

    controller.registration.choose_roles()

    controller.registration.click_registration_button()

    # Checking that the email is already being used. If true = test skipped
    if controller.registration.check_waring_email_already_in_use():
        pytest.skip("Skipped because email is already registered. Ignore it")
    else:
        pass

    controller.session.login(user)

    controller.session.check_if_login_was_successful()
