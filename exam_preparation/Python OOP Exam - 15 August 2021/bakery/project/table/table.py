from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def table_number(self):
        ...

    @table_number.setter
    @abstractmethod
    def table_number(self, value):
        ...
    # @property
    # def table_number(self):
    #     return self.__table_number
    #
    # @table_number.setter
    # def table_number(self, value):
    #     if value not in range(self.minimum, self.maximum + 1):
    #         raise ValueError(f"{self.__class__.__name__} table's number must be between"
    #                          f" {self.minimum} and {self.maximum} inclusive!")
    #     self.__table_number = value
    #
    # @property
    # @abstractmethod
    # def minimum(self):
    #     ...
    #
    # @property
    # @abstractmethod
    # def maximum(self):
    #     ...

    def reserve(self, number_of_people):
        if number_of_people <= self.capacity:
            self.is_reserved = True
            self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        # TODO check if the calculations are correct
        # Which brackets are the right ones for the task?
        return sum(d.price for d in self.drink_orders) + sum(f.price for f in self.food_orders)

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"
