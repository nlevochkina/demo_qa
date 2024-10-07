import pytest

from models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        """
        Проверки на метод check_quantity
        """
        assert product.check_quantity(10) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False

    @pytest.mark.parametrize("quantity", [10, 1000, 1001])
    def test_product_buy(self, product, quantity):
        """
        Проверки на метод buy
        Проверяем результат, если quantity=10 и quantity=1001
        """
        product.buy(quantity)

    def test_product_buy_more_than_available(self, product, quantity=1001):
        """
        Проверяем получение ошибки ValueError при попытке купить больше, чем есть в наличии
        """
        product.buy(quantity)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
