import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def sample_products() -> None:
    """Фикстура: создаём несколько базовых Product для тестов"""
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return [p1, p2, p3]


@pytest.fixture
def category_with_products(sample_products):
    """Фикстура: категория, в которую добавлены sample_products"""
    cat = Category(name="Смартфоны", description="Категория смартфонов")
    for p in sample_products:
        cat.add_product(p)
    return cat


@pytest.fixture
def sample_smartphones():
    """Фикстура: несколько экземпляров Smartphone"""
    s1 = Smartphone("S1", "desc S1", 100.0, 1, 95.0, "S1Model", 128, "Black")
    s2 = Smartphone("S2", "desc S2", 200.0, 2, 96.0, "S2Model", 256, "White")
    return [s1, s2]


@pytest.fixture
def sample_grasses():
    """Фикстура: несколько LawnGrass (экземпляров газонной травы)"""
    g1 = LawnGrass("Grass1", "desc", 10.0, 2, "Россия", "7 дней", "Зеленый")
    g2 = LawnGrass("Grass2", "desc", 12.5, 3, "США", "5 дней", "Темно-зеленый")
    return [g1, g2]


@pytest.fixture
def category_with_smartphones(sample_smartphones):
    """Категория, в которую добавлены смартфоны (подкласс Product)"""
    cat = Category(name="Smartphones", description="Категория смартфонов (subclass)")
    for s in sample_smartphones:
        cat.add_product(s)
    return cat


@pytest.fixture
def mixed_category(sample_products, sample_smartphones):
    """Смешанная категория: product + smartphone"""
    cat = Category("Mixed", "Смешанная категория")
    cat.add_product(sample_products[0])  # базовый Product
    for s in sample_smartphones:
        cat.add_product(s)  # Smartphone — подкласс
    return cat


@pytest.fixture
def category_with_three_products():
    """Категория с тремя продуктами для проверки среднего ценника"""
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 220000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 200000.0, 14)
    cat = Category("Тестовая категория", "Описание категории", [p1, p2, p3])
    return cat


@pytest.fixture
def empty_category():
    """Категория без товаров — для проверки ZeroDivisionError"""
    return Category("Пустая категория", "Нет товаров", [])
