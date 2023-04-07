from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    MEMBERS_COUNT = 2

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, self.MEMBERS_COUNT)
        self.room_cost = 30
        self.children = list(children)
        self.members_count += len(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.calculate_expenses(self.appliances, self.children)