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
