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
