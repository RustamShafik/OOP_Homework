def test_product_init(product_one):
    assert product_one.name == "Samsung S24 Ultra"
    assert product_one.description == ("Замечательный новый "
                                       "смартфон Samsung S24 Ultra")
    assert product_one.price == 100000.50
    assert product_one.quantity == 50
