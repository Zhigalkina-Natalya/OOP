from typing import Optional

from src.product import Product


class Category:
    name: str
    description: str
    products: Optional[list[Product]]
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

        self.products = products

        Category.category_count += 1
        Category.product_count += len(self.products)


# def add_product(self, product: Product) -> None:
#     if not isinstance(product, Product):
#         raise TypeError("product должен быть Product")
#     self.products.append(product)
#     Category.category_count += 1
#
# def remove_product(self, product: Product) -> None:
#     self.products.remove(product)
#     Category.product_count -= 1
