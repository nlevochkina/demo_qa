import pytest
from selene import browser, be, have
@pytest.mark.parametrize("teardown", [True])
def test_search(open_browser_with_teardown):
    browser.element('[name="q"]').should(be.blank).type('@!@*$$#').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
