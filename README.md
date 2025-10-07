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
----------------|-----------------------------------------------------------------------------
 category.py    | *class Category:*                                                           
 category_iterator.py    | *class CategoryIterator:*                                                   
 product.py    | *class Product(BaseProduct):*, *class Smartphone(Product):*, *class LawnGrass(Product):* 
 product.py   | Функциональность: *__init__*, *__str__*, *__add__*, *@classmethod / new_product(cls,..)*, *@property / price(self)*, *@price.setter* 
 base_product.py| Абстрактный класс: *class BaseProduct(ABC):* + Абстрактный метод
 print_mixin.py| *class PrintMixin():*
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

## Модуль base_product.py:
### *class BaseProduct(ABC):*

```
Создан базовый абстрактный класс с именем BaseProduct, который станет родительским для класса продуктов.
Классы «Smartphone» и «LawnGrass» остаются наследниками класса Product и тем самым наследуют все свойства абстрактного класса.
```

## Модуль product.py:
### *class Product(BaseProduct):*

```
class Product(BaseProduct):
    name: str
    description: str
    price: Union[Decimal, float, str]
    quantity: int
```
### *class Smartphone(Product):*

```
class Smartphone(Product):
    name: str,
    description: str,
    price: Union[Decimal, float, str],
    quantity: int,
    efficiency: Union[float, int],
    model: str,
    memory: int,
    color: str
```

### *class LawnGrass(Product):*

```
class LawnGrass(Product):
    name: str
    description: str
    price: Union[Decimal, float, str]
    quantity: int,
    country: str,
    germination_period: str,
    color: str
```
### *def __add__(self, other)*

```
Складывает только из одинаковых классов продуктов.
При попытке сложения объекты разных классов выбрасывается ошибка TypeError
```

### *@classmethod*
### *def new_product(cls, data, existing_products)*

```commandline
Создаёт новый продукт из словаря.
Если продукт с таким же именем уже есть в списке existing_products:
  - увеличивает количество (quantity)
  - выбирает более высокую цену
```

## Модуль print_mixin.py.py:
### *class PrintMixin():*

```
Класс-миксин, который при создании объекта, то есть при работе метода __init__,
печатает в консоль информацию о том, от какого класса и с какими параметрами был создан объект.
Например:
Product('Продукт1', 'Описание продукта', 1200, 10)
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
