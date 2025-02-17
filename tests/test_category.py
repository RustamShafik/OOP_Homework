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
