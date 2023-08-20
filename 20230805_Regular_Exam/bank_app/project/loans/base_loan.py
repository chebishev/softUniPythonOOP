from abc import ABC, abstractmethod


class BaseLoan(ABC):
    PERCENTAGE = 0

    @abstractmethod
    def __init__(self, interest_rate, amount):
        self.interest_rate = interest_rate
        self.amount = amount

    @property
    def get_percentage(self):
        return self.PERCENTAGE

    def increase_interest_rate(self):
        self.interest_rate += self.get_percentage
