from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    RECEIPT_ID = 0
    VALID_MEALS = {
        "Starter": Starter,
        "Dessert": Dessert,
        "MainDish": MainDish
    }

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.current_shopping_cart = {}

    @staticmethod
    def get_next_id():
        FoodOrdersApp.RECEIPT_ID += 1
        return FoodOrdersApp.RECEIPT_ID

    def get_client(self, phone_number):
        return [c for c in self.clients_list if c.phone_number == phone_number][0]

    def check_shopping_cart(self, client):
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

    def check_menu_ready(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def register_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        self.check_menu_ready()
        return '\n'.join(str(meal.details()) for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        self.check_menu_ready()

        try:  # get the client if exists
            client = self.get_client(client_phone_number)
        except IndexError:  # create a new client if the number is not in the list
            self.register_client(client_phone_number)
            client = self.get_client(client_phone_number)

        meals_to_order = []
        current_bill = 0

        meal_names = [m.name for m in self.menu]  # get the meal names from the menu
        for meal_name, quantity in meal_names_and_quantities.items():
            if meal_name not in meal_names:
                raise Exception(f"{meal_name} is not on the menu!")

            current_meal = [m for m in self.menu if m.name == meal_name][0]
            if current_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {current_meal.__class__.__name__}: {meal_name}!")

            meals_to_order.append(current_meal)
            current_bill += current_meal.price * quantity
            self.current_shopping_cart[meal_name] = quantity

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.get_client(client_phone_number)

        self.check_shopping_cart(client)  # raises exception if shopping cart is empty

        for meal_name, quantity in self.current_shopping_cart.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += quantity

        client.shopping_cart = []
        client.bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.get_client(client_phone_number)
        self.check_shopping_cart(client)  # raises exception if shopping cart is empty

        receipt_id = self.get_next_id()
        total_paid_money = client.bill
        client.bill = 0
        client.shopping_cart = []

        return f"Receipt #{receipt_id} with total amount of {total_paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
