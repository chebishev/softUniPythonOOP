from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room
from project.appliances.fridge import Fridge


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, self.budget, self.members_count)
        self.budget = pension_one + pension_two
        self.members_count = 2
        self.room_cost = 15
        self.appliances = [TV, Fridge, Stove] * self.members_count
