from typing import Iterator, Optional

from src.product import Product


class Category:
    name: str
    description: str
    __products: Optional[list[Product]]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None) -> None:
        self.name = name
        self.description = description
        if products is None:
            products = []
        else:
            products = list(products)

        for product in products:
            if not isinstance(product, Product):
                raise TypeError("Каждый элемент в products должен быть экземпляром Product")

        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product")
        if self.__products is None:
            self.__products = [product]
        else:
            self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """
        Геттер: возвращает строку со всеми продуктами в категории.
        """
        result = ""
        if self.__products is not None:
            for product in self.__products:
                result += str(product) + "\n"
        return result.strip()

    def __str__(self) -> str:
        total = 0
        if self.__products is not None:
            for p in self.__products:
                total += int(p.quantity)
        return f"{self.name}, количество продуктов: {total} шт."

    def __iter__(self) -> Iterator[Product]:
        return iter(self.__products)

    def get_products(self) -> list[Product]:
        return list(self.__products)
