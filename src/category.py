from typing import List
from src.product import Product


class Category:
    name: str
    description: str
    products: List[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str,
                 products: List[Product] = None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.product_count += len(products) if products is not None else 0
        Category.category_count += 1

    def add_product(self, product: Product):
        self.__products.append(product)
    
    @property
    def products(self):
        list = []
        for product in self.__products:
            list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return list

    @property
    def products_list(self):
        return self.__products

