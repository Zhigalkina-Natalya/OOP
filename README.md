# Учебный проект по введению в ООП

## Описание

```
В рамках домашних заданий прорабатываем использование классов и объектов на основе популярной темы e-commerce.
```


## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/Zhigalkina-Natalya/coursework_1
```

2. Установите зависимости:

```
Используйте инструмент Poetry.
Запустите команду poetry install в терминале, находясь в корневом каталоге вашего проекта.
```

## Содержание файлов:

Название модуля | Содержание модуля                                                          
----------------|---------------------------------------------------------------------------
 category.py    | *class Category:*
 product.py    | *class Product:*
 utils.py    | *read_json*, *create_objects_from_json*

 
## Пример работы функций:

## Модуль utils:

### *read_json*

```
Загружает данные из JSON-файла и возвращает их в виде списка словарей.
Args:
    filename (str): Имя JSON-файла, который лежит в папке `data` на уровень выше `src`.
Returns:
    list[dict[str, Any]]: Список словарей, загруженных из JSON-файла.
```


### *create_objects_from_json*

```
Преобразует список словарей с категориями и продуктами в объекты `Category` и `Product`.
Args:
    data (list[dict[str, Any]]): Список словарей, каждый из которых должен содержать ключ "products"
                                 со списком словарей для продуктов.
Returns:
    list[Category]: Список объектов `Category`, каждый из которых содержит список объектов `Product`.
```

## Модуль product.py:
### *class Product:*

```
class Product:
    name: str
    description: str
    price: Union[Decimal, float, str]
    quantity: int
```


## Модуль category.py:
### *class Category:*

```
class Category:
    name: str
    description: str
    products: Optional[list[Product]]
    category_count: int = 0
    product_count: int = 0
```


## Инструкция по запуску тестирования

1. Установите зависимости через Poetry с добавлением в отдельную группу: `poetry add --group dev pytest`
2. Запустите тесты: `pytest`
3. Результаты тестов будут выведены в консоль.

## Инструкция по инструменту оценки качества тестирования.

1. В pytest для анализа покрытия кода надо поставить библиотеку pytest-cov.

- Через poetry добавить в отдельную группу: `poetry add --group dev pytest-cov`

2. Запустить тесты с оценкой покрытия, можно следующими командами:

- `pytest --cov` — при активированном виртуальном окружении.
- `poetry run pytest --cov`  — через poetry.
- `pytest --cov=src --cov-report=html`  — чтобы сгенерировать отчет о покрытии в HTML-формате, где src — пакет c
  модулями, которые тестируем.
- Отчет покрытия будет сгенерирован в папке htmlcov и храниться в файле с названием index.html.

## Автор

Жигалкина Наталья
