from typing import Iterator, Optional

from src.base_entity import BaseEntity
from src.product import Product


class Category(BaseEntity):
    name: str
    description: str
    __products: Optional[list[Product]]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[list[Product]] = None) -> None:
        super().__init__(name, description)
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
        """
        Добавляет продукт в категорию. Разрешены только Product и его наследники.
        Проверки выполняем с использованием одновременно isinstance и issubclass (через product._class_).
        """
        # 1) Проверяем, что передан именно экземпляр (а не, например, строка или число)
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или их наследники (ожидался экземпляр)")

        # 2) Дополнительная проверка с использованием issubclass: удостоверимся,
        # что класс переданного объекта действительно является подклассом Product.
        if not issubclass(product.__class__, Product):
            raise TypeError("Класс объекта не является подклассом Product")

        # 3) если проверки пройдены — добавляем в список
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

    def middle_price(self):
        try:
            return sum(p.price for p in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0

    def to_dict(self) -> dict:
        """Минимальное преобразование — реализуем требуемый абстрактный метод."""
        products = self.get_products()
        return {
            "name": self.name,
            "description": self.description,
            "products": [p.name for p in products],
        }
