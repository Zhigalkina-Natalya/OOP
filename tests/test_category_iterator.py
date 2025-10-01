import pytest

from src.category import Category
from src.category_iterator import CategoryIterator


def test_category_iterator_iterates_all_products(category_with_products, sample_products):
    """Проверяем, что CategoryIterator возвращает все продукты"""
    iterator = CategoryIterator(category_with_products)
    products_from_iter = list(iterator)
    assert products_from_iter == sample_products


def test_category_iterator_stop_iteration(category_with_products):
    """Проверяем, что после окончания генерации вызывается StopIteration"""
    iterator = CategoryIterator(category_with_products)
    # проходим все продукты
    for _ in range(len(category_with_products.get_products())):
        next(iterator)
    # теперь должно вызвать StopIteration
    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_empty_category():
    """Проверяем работу итератора для пустой категории"""
    empty_cat = Category(name="Пустая", description="Нет продуктов", products=[])
    iterator = CategoryIterator(empty_cat)
    with pytest.raises(StopIteration):
        next(iterator)
