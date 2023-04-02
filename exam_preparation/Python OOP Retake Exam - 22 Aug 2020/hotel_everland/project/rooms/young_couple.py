from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.appliances.fridge import Fridge


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, self.budget, self.members_count)
        self.budget = salary_one + salary_two
        self.members_count = 2
        self.room_cost = 20
        self.appliances = [TV, Fridge, Laptop] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)