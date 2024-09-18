import pytest
from selene import browser, be, have
@pytest.mark.parametrize("teardown", [False])
def test_search(open_browser_with_teardown):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
