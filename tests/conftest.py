import pytest

from src.category import Category
from src.product import LawnGrass, Product


@pytest.fixture
def category_one():
    return Category(
        name="Смартфон",
        description="Замечательный новый смартфон",
        products=[
            Product(
                "Samsung S24 Ultra",
                "Замечательный новый смартфон Samsung S24 Ultra",
                100000.50,
                50,
            ),
            Product("Siemens A50",
                    "Очень старый телефон Siemens A50", 300, 10),
        ],
    )


@pytest.fixture
def product_one():
    return Product(
        name="Samsung S24 Ultra",
        description="Замечательный новый смартфон Samsung S24 Ultra",
        price=100000.50,
        quantity=50,
    )


@pytest.fixture
def product_two():
    return Product(
        name="Playstation 5 Slim",
        description="Модернизированная версия PS5",
        price=49000.00,
        quantity=12,
    )


@pytest.fixture
def product_three():
    return LawnGrass(
        name="Трава-мурава",
        description="Прекрасная трава-мурава",
        price=490.00,
        quantity=32,
        country="Sweden",
        germination_period="1 год",
        color="желтый",
    )


@pytest.fixture
def non_product_item():
    return 5  # или любой другой объект, не являющийся Product

@pytest.fixture
def no_products_category():
    return Category("Пустая категория", "Категория без продуктов", [])

