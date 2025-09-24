import json
from unittest.mock import mock_open, patch

from src.category import Category
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
    cat = categories[0]
    assert isinstance(cat, Category)
    assert cat.name == "Телевизоры"

    # Проверяем строковое представление геттера products
    output = cat.products
    expected_output = "LG, 50000.0 руб. Остаток: 2 шт."
    assert output == expected_output

    # Дополнительно можно проверить, что в строке есть все данные
    assert "LG" in output
    assert "50000.0" in output
    assert "2" in output
