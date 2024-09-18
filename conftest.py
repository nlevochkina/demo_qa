import pytest
from selene import browser


@pytest.fixture
def set_browser_size():
    browser.driver().set_window_size(1000, 800)


@pytest.fixture
def open_browser():
    browser.open_url('https://google.com')


@pytest.fixture
def open_browser_with_message():
    browser.open_url('https://google.com')
    yield
    print('По вашему запросу нет полезных результатов')
