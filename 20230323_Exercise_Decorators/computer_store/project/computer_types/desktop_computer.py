from horse_racings.project import Computer


class DesktopComputer(Computer):
    VALID_PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    MAX_RAM = 128

    @staticmethod
    def computer_type():
        return "desktop computer"

    @property
    def valid_processors(self):
        return self.VALID_PROCESSORS

    @property
    def max_ram(self):
        return self.MAX_RAM
