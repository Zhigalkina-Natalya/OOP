from decimal import Decimal

import pytest

from src.category import Category
from src.product import Product, Smartphone


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
    assert "15000" in output
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


def test_category_str_returns_correct_total(category_with_products, sample_products):
    """Проверяем, что __str__ возвращает корректное количество продуктов"""
    total_quantity = sum(p.quantity for p in sample_products)
    expected_str = f"{category_with_products.name}, количество продуктов: {total_quantity} шт."
    assert str(category_with_products) == expected_str


def test_category_str_empty_category():
    """Проверяем, что __str__ корректно работает, если продуктов нет"""
    empty_cat = Category("Пустая категория", "Описание пустой категории", products=[])
    expected_str = f"{empty_cat.name}, количество продуктов: 0 шт."
    assert str(empty_cat) == expected_str


def test_category_add_accepts_subclasses_and_base(category_with_products, sample_smartphones):
    """
    Category.add_product должен принимать Product и его наследников (Smartphone).
    Проверяем, что добавление смартфона в категорию с базовыми product работает.
    """
    cat = category_with_products
    s = sample_smartphones[0]
    cat.add_product(s)  # не должно бросать
    out = cat.products
    assert s.name in out


def test_category_add_rejects_non_product(category_with_products):
    """Попытка добавить не-Product объект (строка) или класс должна вызвать TypeError"""
    cat = category_with_products
    with pytest.raises(TypeError):
        cat.add_product("not a product")
    # передача класса, а не экземпляра
    with pytest.raises(TypeError):
        cat.add_product(Smartphone)


def test_category_init_rejects_non_product_in_list():
    """Category конструктор должен выбрасывать TypeError, если в initial list есть не-Product"""
    with pytest.raises(TypeError):
        Category("Bad", "desc", ["string", 123])


def test_middle_price_correct_average(category_with_three_products):
    """
    Тест проверяет, что метод middle_price возвращает правильное среднее значение
    для категории с несколькими продуктами.
    """
    expected = (Decimal("180000") + Decimal("220000") + Decimal("200000")) / 3
    result = category_with_three_products.middle_price()

    assert result == expected


def test_middle_price_empty_returns_zero(empty_category):
    """
    Тест проверяет, что при отсутствии товаров возвращается 0,
    а не возникает ошибка деления на ноль.
    """
    result = empty_category.middle_price()
    assert result == 0
