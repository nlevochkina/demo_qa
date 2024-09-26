import os

from selenium.webdriver.common.by import By
from selene import browser, be, have


def test_fill_out_the_form(open_browser_demo_qa):
    browser.open('https://demoqa.com/automation-practice-form')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    # WHEN

    browser.element('#firstName').should(be.blank).type('Natalia')
    assert browser.element('#firstName').get_attribute('value') == 'Natalia'
    browser.element('#lastName').should(be.blank).type('La')
    browser.element('#userEmail').should(be.blank).type('natalia@mail.ru')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']//option[@value='0']").click()
    browser.driver.find_element(By.XPATH,
                                "//*[@class='react-datepicker__year-select']//option[@value='1990']").click()
    browser.driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012').click()

    browser.element('#subjectsInput').type('Computer Science').press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').should(be.blank).type('Moscow Street, 56, Moscow, Russia')

    image_path = os.path.abspath('./images/sun.jpeg')
    browser.element('#uploadPicture').send_keys(image_path)

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Karnal')).click()

    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Natalia La',
            'natalia@mail.ru',
            'Female',
            '1234567890',
            '12 January,1990',
            'Computer Science',
            'Sports',
            'sun.jpeg',
            'Moscow Street, 56, Moscow, Russia',
            'Haryana Karnal'
        )
    )
