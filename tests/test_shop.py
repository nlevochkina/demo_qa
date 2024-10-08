import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


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

    @pytest.mark.parametrize("quantity", [10, 55, 1000])
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
        try:
            product.buy(quantity)
        except ValueError:
            assert 'Продукта не хватает'


class TestCart:

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
        assert product not in cart.products

    def test_cart_remove_more_product(self, cart, product):
        """
        Удаляем больше товаров, чем есть в корзине
        """
        cart.add_product(product)
        cart.remove_product(product, remove_count=2)
        assert product not in cart.products

    def test_cart_remove_one_product(self, cart, product):
        """
        Удаляем один товар из корзины
        """
        cart.add_product(product, buy_count=2)
        cart.remove_product(product, remove_count=1)
        assert cart.products[product] == 1

    def test_cart_remove_non_exist_product(self, cart, product):
        """
        Удаляем товар в корзине, которого нет
        """
        assert product not in cart.products
        with pytest.raises(ValueError):
            cart.remove_product(product, remove_count=1)

    def test_clear_cart_with_products(self, cart, product):
        """
        Очищаем корзину, в которой есть товары
        """
        cart.add_product(product, buy_count=800)
        assert cart.products[product] == 800
        cart.clear(product)
        assert product not in cart.products

    def test_clear_cart_without_products(self, cart, product):
        """
        Очищаем корзину, в которой нет товаров
        """
        assert product not in cart.products
        with pytest.raises(ValueError):
            cart.clear(product)

    def test_get_total_price_in_cart(self, cart, product):
        """
        Считаем итоговую стоимость товаров в корзине
        """
        cart.add_product(product, buy_count=15)
        cart.get_total_price()

    def test_get_total_price_empty_cart(self, cart, product):
        """
        Считаем итоговую стоимость товаров в пустой корзине
        """
        assert cart.get_total_price() == 0

    def test_cart_buy_products(self, product, cart):
        """
        Покупаем товары
        """
        cart.add_product(product, buy_count=5)
        cart.buy()

    def test_cart_buy_more_quantity_products(self, product, cart):
        """
        Покупаем больше товаров, чем есть в наличии
        """
        cart.add_product(product, buy_count=1001)
        with pytest.raises(ValueError):
            cart.buy()
