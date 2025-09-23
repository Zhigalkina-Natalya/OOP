import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(sample_products):
    """Проверяем корректность инициализации Category"""
    category = Category("Смартфоны", "Описание категории", sample_products)
    assert category.name == "Смартфоны"
    assert category.description == "Описание категории"
    output = category.products
    for product in sample_products:
        assert product.name in output
        assert str(product.price) in output
        assert str(product.quantity) in output


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


def test_add_product_invalid_type_raises():
    """Добавление в категорию объекта не Product должно вызывать TypeError"""
    category = Category("Гаджеты", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product(123)  # число вместо Product
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_category_empty_products_list():
    """Категория без продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая", "Нет товаров", [])
    output = category.products
    assert output == ""  # пустая строка при отсутствии товаров
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_none_products():
    """Категория с products=None должна корректно инициализироваться"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Нет товаров", "Описание")  # products=None по умолчанию
    output = category.products
    assert output == ""  # геттер возвращает пустую строку
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product_changes_count(sample_products):
    """Проверяем добавление продукта после инициализации"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Гаджеты", "Описание", [])
    assert Category.product_count == 0

    new_product = Product("Наушники", "Bluetooth", 15000.0, 20)
    category.add_product(new_product)

    output = category.products
    assert "Наушники" in output
    assert "15000.0" in output
    assert "20" in output
    assert Category.product_count == 1


def test_products_property_format(sample_products):
    """Проверяем правильный формат строки, возвращаемой геттером products"""
    category = Category("Смартфоны", "Описание категории", sample_products)
    output = category.products
    expected_lines = [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in sample_products]
    expected_output = "\n".join(expected_lines)
    assert output == expected_output


def test_add_multiple_products(sample_products):
    """Проверяем добавление нескольких продуктов через add_product"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Гаджеты", "Описание", [])
    new_products = [Product("Наушники", "Bluetooth", 15000.0, 20), Product("Клавиатура", "Механика", 7000.0, 10)]
    for p in new_products:
        category.add_product(p)

    output = category.products
    for p in new_products:
        assert f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." in output

    assert Category.product_count == len(new_products)
