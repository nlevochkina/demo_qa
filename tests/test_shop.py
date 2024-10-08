import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def product_fruit():
    return Product("apple", 50, "This is a fruit", 500)


@pytest.fixture
def cart():
    return Cart()


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
        Проверяем результат c разными quantity
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

    def test_add_product_to_cart(self, cart, product):
        """
        Добавлем товары в корзину
        """
        cart.add_product(product, buy_count=1)
        assert cart.products[product] == 1

        cart.add_product(product, buy_count=2)
        assert cart.products[product] == 3

    def test_cart_remove_all_product(self, cart, product):
        """
        Удаляем все позиции товара из корзины
        """
        cart.add_product(product, buy_count=2)
        cart.remove_product(product)
        assert cart.products[product] == 0

    def test_cart_remove_one_product(self, cart, product):
        """
        Удаляем один товар из корзины
        """
        cart.add_product(product, buy_count=2)
        cart.remove_product(product, remove_count=1)
        assert cart.products[product] == 1

    def test_cart_remove_non_existent_product(self, cart, product):
        """
        Удаляем один товар из корзины
        """
        cart.add_product(product)
        cart.remove_product(product, remove_count=2)
        # with pytest.raises(ValueError):
