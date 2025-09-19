import json
from pathlib import Path
from typing import Any

from src.category import Category
from src.product import Product


def read_json(filename: str) -> list[dict[str, Any]]:
    """Загружает данные из JSON-файла и возвращает их в виде списка словарей"""
    # Папка data лежит на уровень выше src
    base_path = Path(__file__).parent.parent / "data"
    full_path = base_path / filename

    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def create_objects_from_json(data: list[dict[str, Any]]) -> list[Category]:
    """Преобразует список словарей с категориями и продуктами в объекты `Category` и `Product`."""
    categories = []
    for d in data:
        products = []
        for prod in d["products"]:
            products.append(Product(**prod))
        d["products"] = products
        categories.append(Category(**d))

    return categories


if __name__ == "__main__":
    row_data = read_json("products.json")
    print(row_data)

    categories_data = create_objects_from_json(row_data)
    print(categories_data)
    print(categories_data[0].name)
    print(categories_data[0].products)
