from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    VALID_TYPE_FOOD = {"Bread": Bread,
                       "Cake": Cake
                       }

    VALID_TYPE_DRINK = {
        "Water": Water,
        "Tea": Tea
    }

    VALID_TABLE_TYPES = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    def add_food(self, food_type, name, price):
        given_name = [n for n in self.food_menu if n.name == name]
        if food_type in ["Bread", "Cake"] and not given_name:
            self.food_menu.append(self.VALID_TYPE_FOOD[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if drink_type in self.VALID_TYPE_DRINK:
            for drink in self.drinks_menu:
                if drink.name == name:
                    raise Exception(f"{drink.__class__.__name__} {name} is already in the menu!")
            else:
                self.drinks_menu.append(self.VALID_TYPE_DRINK[drink_type](name, portion, brand))
                return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")
        else:
            if table_type in self.VALID_TABLE_TYPES:
                self.tables_repository.append(self.VALID_TABLE_TYPES[table_type](table_number, capacity))
                return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        available_table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people]

        if not available_table:
            return f"No available table for {number_of_people} people"

        available_table[0].reserve(number_of_people)
        return f'Table {available_table[0].table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number, *food_name):
        result = [f'Table {table_number} ordered:']
        result1 = [f'{self.name} does not have in the menu:']
        available_table = [t for t in self.tables_repository if t.table_number == table_number]

        if not available_table:
            return f'Could not find table {table_number}'

        for food in food_name:
            for f in self.food_menu:
                if food == f.name:
                    available_table[0].food_orders.append(f)
                    result.append(f'- {f.name}: {f.portion:.2f}g - {f.price:.2f}lv')
                    break
            else:
                result1.append(food)
        result.extend(result1)
        return '\n'.join(result)

    def order_drink(self, table_number, *drink_name):
        drinks_not_in_menu = []
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        result = [f"Table {table_number} ordered:"]

        for d in drink_name:
            for drink in self.drinks_menu:
                if d == drink.name:
                    result.append(table.order_drink(drink))
                    break
            else:
                drinks_not_in_menu.append(d)

        result.append(f"{self.name} does not have in the menu:")
        result.extend(drinks_not_in_menu)
        return '\n'.join(result)

    def leave_table(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table_number}\n" \
                   f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        return '\n'.join([t.free_table_info() for t in self.tables_repository if not t.is_reserved])

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
