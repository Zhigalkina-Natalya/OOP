from decimal import Decimal

import pytest

from src.product import Product


def test_product_initialization():
    """Проверяем корректность инициализации Product"""
    product = Product("Test", "Описание", 9999.99, 10)
    assert product.name == "Test"
    assert product.description == "Описание"
    assert product.price == Decimal("9999.99")
    assert product.quantity == 10


def test_product_negative_quantity_raises():
    """Тест покрывает raise ValueError"""
    with pytest.raises(ValueError):
        Product("D", "desc", 1.0, -1)


def test_price_setter_increase():
    """Увеличение цены"""
    product = Product("Test", "Описание", 100.0, 1)
    product.price = 150.0
    assert product.price == Decimal("150.0")


def test_price_setter_negative_or_zero(capfd):
    """Попытка установить 0 или отрицательную цену"""
    product = Product("Test", "Описание", 100.0, 1)
    product.price = 0
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == Decimal("100.0")

    product.price = -50
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == Decimal("100.0")


def test_price_setter_decrease_confirm_yes(monkeypatch):
    """Снижение цены с подтверждением 'y'"""
    product = Product("Test", "Описание", 100.0, 1)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 50.0
    assert product.price == Decimal("50.0")


def test_price_setter_decrease_confirm_no(monkeypatch, capfd):
    """Снижение цены с отказом 'n'"""
    product = Product("Test", "Описание", 100.0, 1)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 50.0
    out, _ = capfd.readouterr()
    assert "Изменение отменено" in out
    assert product.price == Decimal("100.0")


def test_new_product_creates_new():
    data = {"name": "P1", "description": "Desc", "price": 100.0, "quantity": 5}
    prod = Product.new_product(data)
    assert isinstance(prod, Product)
    assert prod.name == "P1"
    assert prod.quantity == 5
    assert prod.price == Decimal("100.0")


def test_new_product_updates_existing_higher_price():
    existing = [Product("P1", "Desc", 100.0, 5)]
    data = {"name": "P1", "description": "Desc", "price": 150.0, "quantity": 3}
    prod = Product.new_product(data, existing)
    assert prod is existing[0]
    assert prod.quantity == 8  # 5+3
    assert prod.price == Decimal("150.0")  # новая цена выше


def test_new_product_updates_existing_lower_price():
    """Проверяем, что существующий продукт обновляет количество, но цена не снижается"""
    existing = [Product("P1", "Desc", 100.0, 5)]
    data = {"name": "P1", "description": "Desc", "price": 50.0, "quantity": 2}

    prod = Product.new_product(data, existing)
    assert prod is existing[0]
    assert prod.quantity == 7  # количество увеличилось
    assert prod.price == Decimal("100.0")  # цена не изменилась


def test_str_representation_integer_price():
    """
    Проверяем __str__ для случая, когда цена — целое (например 100),
    чтобы строка совпадала с ожидаемым форматом:
    "Название, 100 руб. Остаток: 5 шт."
    """
    p = Product("TestProduct", "Desc", 100, 5)  # цена 100 -> Decimal('100')
    expected = "TestProduct, 100 руб. Остаток: 5 шт."
    assert str(p) == expected


def test_str_representation_float_price_shows_decimal_part():
    """
    Если цена задаётся как float с дробной частью (например 99.99),
    __str__ использует внутреннее __price, поэтому проверяем соответствие.
    """
    p = Product("P2", "Desc", 99.99, 3)
    # внутренняя цена хранится как Decimal(str(99.99)) -> Decimal('99.99')
    assert str(p) == f"P2, {p._Product__price} руб. Остаток: 3 шт."


def test_add_returns_sum_of_price_times_quantity():
    """
    Проверяем __add__: a + b == a.price*a.quantity + b.price*b.quantity (тип Decimal)
    Пример из задания: 100*10 + 200*2 = 1400
    """
    a = Product("a", "desc", 100, 10)  # 100 * 10 = 1000
    b = Product("b", "desc", 200, 2)  # 200 * 2 = 400

    res = a + b
    assert isinstance(res, Decimal)
    assert res == Decimal("1400")


def test_add_returns_decimal_with_non_integer_prices():
    """
    Проверяем сложение, если цены не целые (например 12.50 и 3.40),
    чтобы точность Decimal сохранялась.
    """
    a = Product("x", "d", 12.5, 4)  # 12.5 * 4 = 50.0
    b = Product("y", "d", 3.4, 3)  # 3.4 * 3 = 10.2
    res = a + b
    # ожидаем Decimal('60.2') (возможно Decimal('60.20') — сравниваем через Decimal(str(...)))
    assert isinstance(res, Decimal)
    assert res == Decimal(str(12.5 * 4 + 3.4 * 3))
