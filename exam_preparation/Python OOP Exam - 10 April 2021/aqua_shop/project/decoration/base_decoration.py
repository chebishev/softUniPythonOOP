from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    @abstractmethod
    def __init__(self, comfort, price):
        self.comfort = comfort
        self.price = price

    def __eq__(self, other):
        if self.__class__.__name__ == other.__class__.__name__ and \
                self.comfort == other.comfort and \
                self.price == other.price:
            return True
