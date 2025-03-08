from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def new_product(self):
        pass


class MixinPrint:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.name}, {self.description}, "
            f"{self.price}, {self.quantity})"
        )


class Product(MixinPrint, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        if self.quantity == 0:
            print("Товар с нулевым количеством не может быть добавлен.")
            raise ValueError

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # if type(other) == type(self):
        if isinstance(other, type(self)):
            return (self.quantity * self.price) + (other.quantity * other.price)
        raise TypeError

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
            description=product_data.get("description"),
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency,
        model,
        memory,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
            description=product_data.get("description"),
            efficiency=product_data.get("efficiency"),
            model=product_data.get("model"),
            memory=product_data.get("memory"),
            color=product_data.get("color"),
        )


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country,
        germination_period,
        color,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
            description=product_data.get("description"),
            country=product_data.get("country"),
            germination_period=product_data.get("germination_period"),
            color=product_data.get("color"),
        )
