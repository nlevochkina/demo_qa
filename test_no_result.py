from selene import browser, be, have


def test_search(set_browser_size, open_browser_with_message):
    browser.element('[name="q"]').should(be.blank).type('@!@*$$#').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))
