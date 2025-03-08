import pytest


def test_category_init(category_one):
    assert category_one.name == "Смартфон"
    assert category_one.description == "Замечательный новый смартфон"
    assert len(category_one.products) == 2
    assert category_one.category_count == 1
    assert category_one.product_count == 2
    assert category_one.products_list[0].name == "Samsung S24 Ultra"
    # Используется геттер products_list
    assert category_one.products_list[1].name == "Siemens A50"
    # Используется геттер products_list


def test_add_product(product_two, category_one):
    category_one.add_product(product_two)
    assert len(category_one.products_list) == 3
    assert (
        category_one.products_list[2].name == "Playstation 5 Slim"
    )  # Используется геттер products_list


def test_str_presentation(category_one):
    assert str(category_one) == "Смартфон, количество продуктов: 60 шт."


def test_add_different_class_to_list(category_one, non_product_item):
    with pytest.raises(TypeError):
        category_one.add_product(non_product_item)
def test_zero_division_error(no_products_category):
    assert no_products_category.middle_price() == 0

def test_return_average_price(category_one):
    assert category_one.middle_price() == 50150.25
