from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @staticmethod
    @abstractmethod
    def computer_type():
        pass

    @abstractmethod
    def valid_processors(self):
        pass

    @abstractmethod
    def max_ram(self):
        pass

    @staticmethod
    def is_power_of_two(n):
        return (n != 0) and (n & (n - 1) == 0)

    def calculate_price(self, processor, ram):
        return self.valid_processors[processor] + (int(log2(ram)) * 100)

    def configure_computer(self, processor, ram):
        if processor not in self.valid_processors:
            raise ValueError(
                f"{processor} is not compatible with {self.computer_type()} {self.manufacturer} {self.model}!")

        if not self.is_power_of_two(ram) or not 1 < ram <= self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.computer_type()} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price = self.calculate_price(self.processor, self.ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
