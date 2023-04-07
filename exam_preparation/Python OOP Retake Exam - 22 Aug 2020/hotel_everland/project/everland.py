class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        current_expenses = 0
        for room in self.rooms:
            current_expenses += room.expenses + room.room_cost

        return f"Monthly consumption: {current_expenses:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            current_expenses = room.expenses + room.room_cost
            if room.budget >= current_expenses:
                room.budget -= current_expenses
                result.append(f"{room.family_name} paid {current_expenses:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        result = []
        all_people_in_the_hotel = sum(room.members_count for room in self.rooms)
        result.append(f"Total population: {all_people_in_the_hotel}")
        for room in self.rooms:
            result.append(f"{room.family_name} with {room.members_count} members. "
                          f"Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$")
            if room.children:
                for index in range(len(room.children)):
                    child = room.children[index]
                    result.append(f"--- Child {index + 1} monthly cost: {child.get_monthly_expense()}$")
            if room.appliances:
                appliances_cost = sum([a.cost for a in room.appliances]) * 30
                result.append(f"--- Appliances monthly cost: {appliances_cost:.2f}$")

        return "\n".join(result)
