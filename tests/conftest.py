import pytest
from src.product import Product
from src.category import Category


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
            Product("Siemens A50", "Очень старый телефон Siemens A50",
                    300, 10),
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
