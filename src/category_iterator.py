from typing import Iterator

from src.category import Category
from src.product import Product


class CategoryIterator:
    def __init__(self, category: Category) -> None:
        self._products: list[Product] = category.get_products()
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        return self

    def __next__(self) -> Product:
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    for product in category1:
        print(product)
    print()
    for product in category1:
        print(product)
