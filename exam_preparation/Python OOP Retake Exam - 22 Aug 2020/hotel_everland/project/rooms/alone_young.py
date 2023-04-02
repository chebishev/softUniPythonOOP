from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, self.budget, self.members_count)
        self.budget = salary
        self.members_count = 1
        self.room_cost = 10
        self.appliances = [TV]
