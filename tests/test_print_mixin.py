from src.product import LawnGrass, Product, Smartphone


def test_print_mixin(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"

    Smartphone("S1", "desc S1", 100.0, 1, 95.0, "S1Model", 128, "Black")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(S1, desc S1, 100.0, 1)"

    LawnGrass("Grass1", "desc", 10.0, 2, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Grass1, desc, 10.0, 2)"
