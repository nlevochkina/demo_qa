from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selene import browser, be


def test_fill_out_the_form():
    browser.open('https://demoqa.com/automation-practice-form')

    """
    Заполняем обязательные поля формы
    
    """

    browser.element('#firstName').should(be.blank).type('Наталия').press_enter()
    browser.element('#lastName').should(be.blank).type('Левочкина').press_enter()
    browser.element('#userEmail').should(be.blank).type('natalia@mail.ru').press_enter()
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('790012345678').press_enter()

    """
    Заполняем опциональные поля формы
    
    """

    browser.element('#dateOfBirthInput').click()
    browser.driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
    browser.driver.find_element(By.XPATH, "//option[@value='0']").click()
    browser.driver.find_element(By.CLASS_NAME, 'react-datepicker__year-dropdown-container--select')
    browser.driver.find_element(By.XPATH, "//option[@value='1990']").click()
    browser.driver.find_element(By.CLASS_NAME, 'react-datepicker__month')
    browser.driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012').click()

    # browser.driver.find_element(By.CSS_SELECTOR, 'subjects-auto-complete__value-container subjects-auto-complete__value-container--is-multi css-1hwfws3').send_keys('b' + Keys.ENTER)
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').should(be.blank).type('Москва, улица Московская, дом 56').press_enter()

