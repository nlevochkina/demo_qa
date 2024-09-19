import pytest
from selene import browser


@pytest.fixture(scope='session')
def set_browser_size():
    browser.config.driver_name = "chrome"
    browser.config.window_height = 1000
    browser.config.window_width = 800


@pytest.fixture
def open_browser():
    browser.open('https://google.com')


@pytest.fixture
def open_browser_with_message():
    browser.open('https://google.com')
    yield
    print('По вашему запросу нет полезных результатов')
