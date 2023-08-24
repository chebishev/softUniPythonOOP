from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    PERCENT = 0

    @abstractmethod
    def __init__(self, protection, price):
        self.protection = protection
        self.price = price

    def increase_price(self):
        self.price += self.price * self.PERCENT / 100
