from project.computer_types.computer import Computer


class Laptop(Computer):
    VALID_PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    MAX_RAM = 64

    @staticmethod
    def computer_type():
        return "laptop"

    @property
    def valid_processors(self):
        return self.VALID_PROCESSORS

    @property
    def max_ram(self):
        return self.MAX_RAM
