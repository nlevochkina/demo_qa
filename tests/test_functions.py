from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """

    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    current_time = time(hour=23)
    day = time(6, 0)
    night = time(22, 0)
    if current_time >= day and current_time <= night:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """

    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    current_time = time(hour=16)
    day = time(6, 0)
    night = time(22, 0)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user != None:
        is_dark_theme = dark_theme_enabled_by_user
    elif current_time >= day and current_time <= night:
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"

    for suitable_users in users:
        if suitable_users['name'] == 'Olga':
            print(suitable_users)
            assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    suitable_users = []

    for young_users in users:
        if young_users['age'] < 20:
            suitable_users.append(young_users)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def universal_function(func, *args):
    new_name = func.__name__.replace('_', ' ').title()
    args_unpacked = ''
    for i in args:
        args_unpacked = args_unpacked + i + ', '
    args_unpacked = args_unpacked.rstrip(", ")
    return f'{new_name} [{args_unpacked}]'


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = universal_function(open_browser, f'{browser_name}')
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = universal_function(go_to_companyname_homepage, f'{page_url}')
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = universal_function(find_registration_button_on_login_page, f'{page_url}', f'{button_text}')
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
