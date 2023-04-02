from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, self.budget, self.members_count)
        self.budget = salary_one + salary_two
        self.members_count = 2 + len(children)
        self.room_cost = 30
        self.children = children
        self.appliances = [TV, Fridge, Laptop] * self.members_count
