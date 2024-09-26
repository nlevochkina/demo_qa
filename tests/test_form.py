import os

from selenium.webdriver.common.by import By
from selene import browser, be, have


def test_fill_out_the_form():
    browser.open('https://demoqa.com/automation-practice-form')

    # WHEN

    browser.element('#firstName').should(be.blank).type('Наталия')
    browser.element('#lastName').should(be.blank).type('Левочкина')
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
    browser.element('#currentAddress').should(be.blank).type('Москва, улица Московская, дом 56')

    image = os.path.abspath(os.path.dirname('sun.jpeg'))
    image_path = os.path.join(image, 'images', 'sun.jpeg')
    browser.element('#uploadPicture').send_keys(image_path)

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.text('Karnal')).click()

    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Наталия Левочкина',
            'natalia@mail.ru',
            'Female',
            '1234567890',
            '12 January,1990',
            'Computer Science',
            'Sports',
            'sun.jpeg',
            'Москва, улица Московская, дом 56',
            'Haryana Karnal'
        )
    )
