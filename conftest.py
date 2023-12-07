# -*- coding: utf-8 -*-

import pytest
from fixture.controller import Controller


@pytest.fixture(scope="session")
def controller(request):
    browser_dir = request.config.getoption("--browser_dir")
    fixture = Controller(browser_dir=browser_dir)
    request.addfinalizer(fixture.stop_driver)
    return fixture


def pytest_addoption(parser):
    # parser.addoption("--browser_dir", action="store", default="../geckodriver-v0.24.0-win64/geckodriver.exe")
    parser.addoption("--browser_dir", action="store", default="../geckodriver-v0.33.0-win64/geckodriver.exe")
