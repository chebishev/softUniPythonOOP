from horse_racings.project import Drink
from horse_racings.project import Food
from horse_racings.project import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        result = self.find(product_name)

        if result:
            self.products.remove(result)

    def __repr__(self):
        return '\n'.join(f"{product}: {product.quantity}" for product in self.products)


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
