from horse_racings.project import DesktopComputer
from horse_racings.project import Laptop


class ComputerStoreApp:
    COMPUTER_TYPES = {
        "Desktop Computer": DesktopComputer,
        "Laptop": Laptop
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer not in self.COMPUTER_TYPES:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.COMPUTER_TYPES[type_computer](manufacturer, model)
        self.warehouse.append(computer)
        return computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for computer in self.warehouse:
            if computer.processor == wanted_processor and \
                    computer.ram >= wanted_ram and \
                    computer.price <= client_budget:
                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)
                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")
