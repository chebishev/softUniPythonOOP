from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water


class Bakery:
    VALID_FOODS = {
        "Bread": Bread,
        "Cake": Cake,
    }
    VALID_DRINKS = {
        "Tea": Tea,
        "Water": Water
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        for f in self.food_menu:
            if f.name == name:
                raise Exception(f"{f.__class__.__name__} {name} is already in the menu!")

        if food_type in self.VALID_FOODS:
            food = self.VALID_FOODS[food_type](name, price)
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        for d in self.drinks_menu:
            if d.name == name:
                raise Exception(f"{d.__class__.__name__} {name} is already in the menu!")

        if drink_type in self.VALID_DRINKS:
            drink = self.VALID_DRINKS[drink_type](name, portion, brand)
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        ...

    def reserve_table(self, number_of_people):
        ...

    def order_food(self, table_number, *food_name):
        ...

    def order_drink(self, table_number, *drink_name):
        ...

    def leave_table(self, table_number):
        ...

    def get_free_tables_info(self):
        ...

    def get_total_income(self):
        ...
