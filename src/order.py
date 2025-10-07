from decimal import Decimal
from typing import Dict

from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    """
    Заказ, содержащий один тип товара.
    Создаётся как Order(product, quantity, description='', reduce_stock=True).
    По умолчанию уменьшаем остаток на складе (reduce_stock=True).
    """

    def __init__(self, product: Product, quantity: int, description: str = "", reduce_stock: bool = True) -> None:
        if not isinstance(product, Product):
            raise TypeError("product должен быть экземпляром Product")

        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("quantity должен быть положительным числом")

        if quantity > product.quantity:
            raise ValueError(f"Недостаточно товара на складе: запрошено {quantity}, доступно {product.quantity}")

        name = f"Order_{product.name}"
        desc = description or f"Заказ {quantity} шт. товара {product.name}"

        super().__init__(name=name, description=desc)

        self.product = product
        self.quantity = quantity
        # product.price — Decimal в Product, умножаем на int -> Decimal
        self.total_price = product.price * Decimal(self.quantity)

        if reduce_stock:
            # уменьшаем остаток (встроенная логика). Тесты, которые проверяют остаток — учтут это.
            product.quantity -= self.quantity

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "description": self.description,
            "product": self.product.name,
            "quantity": str(self.quantity),
            "total_price": str(self.total_price),
        }

    def __repr__(self) -> str:
        return f"Order({self.product.name}, {self.quantity}, total={self.total_price})"

    def __str__(self) -> str:
        return f"Заказ: {self.product.name} — {self.quantity} шт., итого {self.total_price} руб."


if __name__ == "__main__":
    p = Product("Молоко", "Описание", "125.5", 10)
    print(p)  # старый вывод -> проверяем, что Product не сломался

    order = Order(p, 3)
    print(order)  # строковое представление заказа
    print("Остаток:", p.quantity)  # ожидаем 7

    # Попытка заказать больше остатка -> ValueError
    try:
        Order(p, 100)
    except ValueError as e:
        print("Ожидаемая ошибка:", e)
