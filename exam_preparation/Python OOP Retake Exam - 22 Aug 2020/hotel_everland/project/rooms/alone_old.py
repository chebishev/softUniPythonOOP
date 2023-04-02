from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        super().__init__(family_name, self.budget, self.members_count)
        self.budget = pension
        self.members_count = 1
        self.room_cost = 10
