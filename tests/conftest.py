import pytest

from src.product import Product


@pytest.fixture
def sample_products() -> None:
    """Фикстура: создаём несколько продуктов для тестов"""
    p1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    p3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return [p1, p2, p3]
