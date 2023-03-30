from horse_racings.project import OpenBooth
from horse_racings.project import PrivateBooth
from horse_racings.project import Gingerbread
from horse_racings.project import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen
    }
    VALID_BOOTHS = {
        "Open Booth": OpenBooth,
        "Private Booth": PrivateBooth
    }

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, type_delicacy, name, price):

        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth, booth_number, capacity):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):

        for booth in self.booths:
            if not booth.is_reserved:
                if booth.capacity >= number_of_people:
                    booth.reserve(number_of_people)
                    return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):
        try:
            booth = [b for b in self.booths if b.booth_number == booth_number][0]
        except IndexError:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = [d for d in self.delicacies if d.name == delicacy_name][0]
        except IndexError:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = [b for b in self.booths if b.booth_number == booth_number][0]
        current_income = booth.get_bill()
        self.income += current_income
        booth.delicacy_orders = []
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth_number}:\n" \
               f"Bill: {current_income:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
