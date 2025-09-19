import json
from unittest.mock import mock_open, patch

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, read_json


def test_read_json_with_mock():
    """Проверяем чтение JSON с помощью mock_open"""
    fake_data = [{"name": "Категория", "description": "Описание", "products": []}]
    mock_file = mock_open(read_data=json.dumps(fake_data, ensure_ascii=False))

    with patch("builtins.open", mock_file):
        result = read_json("products.json")

    assert isinstance(result, list)
    assert result[0]["name"] == "Категория"
    mock_file.assert_called_once()  # проверяем, что файл открывался


def test_create_objects_from_json_with_mock():
    """Проверяем создание объектов из словарей"""
    data = [
        {
            "name": "Телевизоры",
            "description": "Описание",
            "products": [{"name": "LG", "description": "4K", "price": 50000.0, "quantity": 2}],
        }
    ]

    categories = create_objects_from_json(data)

    assert isinstance(categories[0], Category)
    assert categories[0].name == "Телевизоры"
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].products[0].price == 50000.0
