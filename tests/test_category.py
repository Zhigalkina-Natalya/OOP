import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(sample_products):
    """Проверяем корректность инициализации Category"""
    category = Category("Смартфоны", "Описание категории", sample_products)
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    assert len(category.products) == 3
    assert all(isinstance(p, Product) for p in category.products)


def test_category_and_product_count(sample_products):
    """Проверяем подсчёт категорий и продуктов"""
    # Сбрасываем счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Смартфоны", "Описание", sample_products)
    assert isinstance(category1, Category)
    assert Category.category_count == 1
    assert Category.product_count == 3

    product4 = Product("Телевизор", "QLED", 123000.0, 7)
    category2 = Category("Телевизоры", "Описание", [product4])
    assert category2.name == "Телевизоры"
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_category_invalid_product_type_raises():
    """Тест покрывает raise TypeError"""
    with pytest.raises(TypeError):
        Category("Bad", "desc", [123, "not a product"])
