from src.product import Product


def test_product_init(product_one):
    assert product_one.name == "Samsung S24 Ultra"
    assert product_one.description == (
        "Замечательный новый " "смартфон Samsung S24 Ultra"
    )
    assert product_one.price == 100000.50
    assert product_one.quantity == 50


def test_add_new_product():  # Создаем новый экземпляр класса продукта
    product_data = {
        "name": "Samsung Galaxy S24",
        "price": 95000.00,
        "quantity": 25,
        "description": "Самый новый смартфон от Samsung "
        "с улучшенной камерой и процессором.",
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Samsung Galaxy S24"
    assert new_product.quantity == 25


def test_price_lower_than_zero(product_one):
    product_one.price = 175000
    assert product_one.price == 175000
    product_one.price = 0
    assert product_one.price == 175000


def test_adding_products(product_one, product_two):
    assert product_one + product_two == 5588025.0
