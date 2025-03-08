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
        if not isinstance(product, Product):
            # Сначала проверяем, является ли продуктом
            raise TypeError("Можно добавлять только объекты класса Product")
        self.__products.append(product)  # Добавляем только после проверки

    def __str__(self):
        return (
            f"{self.name}, "
            f"количество продуктов: "
            f"{sum(product.quantity for product in self.__products)} шт."
        )

    @property
    def products(self):
        return [str(product) for product in self.__products]

    @property
    def products_list(self):
        return self.__products

    def middle_price(self):
        total_price = 0
        for product in self.__products:
            total_price += product.price
        try:
            average_price = total_price / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0


