import pytest
from selene import browser

@pytest.fixture
def open_browser_with_teardown(teardown):
    browser.open('https://google.com')
    yield
    if teardown:
        print('По вашему запросу нет полезных результатов')