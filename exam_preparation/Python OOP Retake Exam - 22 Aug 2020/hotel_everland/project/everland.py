class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        current_expenses = 0
        for room in self.rooms:
            room.calculate_expenses(room.appliances, room.children)
            current_expenses += room.expenses

        return f"Monthly consumption: {current_expenses}$."

    def pay(self):
        pass

    def status(self):
        pass