from decimal import Decimal
from typing import Union


class Product:
    name: str
    description: str
    __price: Union[Decimal, float, str]  # Decimal из модуля decimal (точность при работе с деньгами)
    quantity: int

    def __init__(self, name: str, description: str, price: Union[Decimal, float, str], quantity: int) -> None:
        self.name = name
        self.description = description
        # Конвертация в Decimal
        if isinstance(price, Decimal):
            self.__price = price
        else:
            self.__price = Decimal(str(price))

        self.quantity = int(quantity)
        if self.quantity < 0:
            raise ValueError("quantity не может быть отрицательным")

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other) -> Union[float, NotImplemented]:
        """
        Складывает только одинаковые типы продуктов (по type())
        При попытке сложения объекты разных классов выбрасывается ошибка TypeError
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать продукты разных классов")
        total = self.price * self.quantity + other.price * other.quantity
        return total

    @property
    def price(self) -> Decimal:
        return Decimal(str(self.__price))

    @price.setter
    def price(self, new_price: Union[Decimal, float, str]) -> None:
        new_price = Decimal(str(new_price))
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < Decimal(str(self.__price)):
            answer = input(f"Цена снижается с {self.__price} до {new_price}. Подтвердите (y/n): ")
            if answer.lower() != "y":
                print("Изменение отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(
        cls, data: dict[str, Union[str, float, int]], existing_products: list["Product"] | None = None
    ) -> "Product":
        """
        Создаёт новый продукт из словаря.
        Если продукт с таким же именем уже есть в списке existing_products:
          - увеличивает количество (quantity)
          - выбирает более высокую цену
        """
        if existing_products is None:
            existing_products = []

        for product in existing_products:
            if product.name == str(data["name"]):  # нашли дубликат
                # Обновляем количество
                product.quantity += int(data["quantity"])
                # Если новая цена выше — обновляем цену
                if Decimal(str(data["price"])) > product.price:
                    product.price = data["price"]
                return product  # возвращаем уже существующий продукт

        # Если дубликатов нет — создаём новый
        return cls(
            name=str(data["name"]),
            description=str(data["description"]),
            price=data["price"],
            quantity=int(data["quantity"]),
        )


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: Union[Decimal, float, str],
        quantity: int,
        efficiency: Union[float, int],
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = float(efficiency)
        self.model = str(model)
        self.memory = int(memory)
        self.color = str(color)


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: Union[Decimal, float, str],
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = str(country)
        self.germination_period = str(germination_period)
        self.color = str(color)
