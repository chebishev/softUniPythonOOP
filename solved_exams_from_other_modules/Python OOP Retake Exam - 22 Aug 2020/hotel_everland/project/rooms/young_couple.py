from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room
from project.appliances.fridge import Fridge


class YoungCouple(Room):
    MEMBERS_COUNT = 2

    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, self.MEMBERS_COUNT)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.calculate_expenses(self.appliances)
