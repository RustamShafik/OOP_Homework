def test_category_init(category_one):
    assert category_one.name == "Смартфон"
    assert category_one.description == "Замечательный новый смартфон"
    assert len(category_one.products) == 2
    assert category_one.category_count == 1
    assert category_one.product_count == 2
    assert category_one.products[0].name == "Samsung S24 Ultra"
    assert category_one.products[1].name == "Siemens A50"
