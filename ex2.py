import datetime
import json


class Pizza:
    __ingred = ['cheese', 'sauce', 'meat', 'vegetables', 'chilli', 'dough']

    def __init__(self, ingredients, size):
        self.ingredients = ingredients
        self.size = size
        self.price = 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int or float) or value <= 0:
            raise Exception("Your price is invalid")
        self.__price = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, list) or not all(item in self.__ingred for item in value):
            raise Exception("Your ingredients is invalid")
        self.__ingredients = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int) or value != 30:
            raise Exception("Your size is invalid")
        self.__size = value

    def add_in(self, value):
        if not isinstance(value, list) or not all(item in self.__ingred for item in value):
            raise Exception("Your ingredients is invalid")
        self.__ingredients = self.__ingredients + value

    def __str__(self):
        k = ''
        for i in self.ingredients:
            k += f'{i}, '
        return f'Your order:\n{self.title}\nIngredients: {k}\nSize: {self.size}cm' \
               f'\nPrice: {self.price}'


class NeapolitanPizza(Pizza):
    title = 'Neapolitan Pizza'

    def __init__(self, ingredients, size):
        super().__init__(ingredients, size)

    def price_change(self):
        if self.size == 30:
            self.price = 200
            for i in self.ingredients:
                self.price += 10
        return self.price

    def __str__(self):
        self.price_change()
        return super().__str__()


class CaliforniaPizza(Pizza):
    title = 'California Pizza'

    def __init__(self, ingredients, size):
        super().__init__(ingredients, size)

    def price_change(self):
        if self.size == 30:
            self.price = 180
            for i in self.ingredients:
                self.price += 10
        return self.price

    def __str__(self):
        self.price_change()
        return super().__str__()


class CheesePizza(Pizza):
    title = 'Sicilian Pizza'

    def __init__(self, ingredients, size):
        super().__init__(ingredients, size)

    def price_change(self):
        if self.size == 30:
            self.price = 220
            for i in self.ingredients:
                self.price += 10
        return self.price

    def __str__(self):
        self.price_change()
        return super().__str__()


class AmericanoPizza(Pizza):
    title = ' Greek Pizza'

    def __init__(self, ingredients, size):
        super().__init__(ingredients, size)

    def price_change(self):
        if self.size == 30:
            self.price = 200
            for i in self.ingredients:
                self.price += 10
        return self.price

    def __str__(self):
        self.price_change()
        return super().__str__()


class MeatPizza(Pizza):
    title = 'Detroit Pizza'

    def __init__(self, ingredients, size):
        super().__init__(ingredients, size)

    def price_change(self):
        if self.size == 30:
            self.price = 210
            for i in self.ingredients:
                self.price += 10
        return self.price

    def __str__(self):
        self.price_change()
        return super().__str__()


class ChicagoPizza(Pizza):
    title = 'Chicago Pizza'

    def __init__(self, ingredients, size):
        super().__init__(ingredients, size)

    def price_change(self):
        if self.size == 30:
            self.price = 240
            for i in self.ingredients:
                self.price += 10
        return self.price

    def __str__(self):
        self.price_change()
        return super().__str__()


def get_pizza():
    today = datetime.date.today()
    with open('menu.json', 'r') as file:
        json_object = json.load(file)
        return eval(json_object[str(today.isoweekday())])


pizza = get_pizza()(['cheese', 'dough'], 30)
pizza.add_in(['meat', 'cheese'])
print(pizza)
