from decimal import Decimal
from typing import Union


class Product:
    name: str
    description: str
    price: Union[Decimal, float, str]  # Decimal из модуля decimal (точность при работе с деньгами)
    quantity: int

    def __init__(self, name: str, description: str, price: Union[Decimal, float, str], quantity: int) -> None:
        self.name = name
        self.description = description
        # Конвертация в Decimal
        if isinstance(price, Decimal):
            self.price = price
        else:
            self.price = Decimal(str(price))

        self.quantity = int(quantity)
        if self.quantity < 0:
            raise ValueError("quantity не может быть отрицательным")
