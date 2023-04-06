from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    MEMBERS_COUNT = 1

    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, self.MEMBERS_COUNT)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(self.appliances)
