from selenium.webdriver.common.by import By
from selene import browser, be


def test_fill_out_the_form():
    browser.open('https://demoqa.com/automation-practice-form')

    """
    Заполняем обязательные поля формы
    
    """

    browser.element('#firstName').should(be.blank).type('Наталия')
    browser.element('#lastName').should(be.blank).type('Левочкина')
    browser.element('#userEmail').should(be.blank).type('natalia@mail.ru')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('790012345678')

    """
    Заполняем опциональные поля формы
    
    """

    browser.element('#dateOfBirthInput').click()
    browser.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']//option[@value='0']").click()
    browser.driver.find_element(By.XPATH,
                                "//*[@class='react-datepicker__year-select']//option[@value='1990']").click()
    browser.driver.find_element(By.CLASS_NAME, 'react-datepicker__day--012').click()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#currentAddress').should(be.blank).type('Москва, улица Московская, дом 56')
    browser.element('#uploadPicture').send_keys('/Users/nlevochkina/PycharmProjects/demo_qa/images/sun.jpeg')

    """
    Отправляем заполненную форму
    
    """
    browser.element('#submit').click()