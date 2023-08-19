from abc import ABC, abstractmethod


class BaseLoan(ABC):

    @abstractmethod
    def __init__(self, interest_rate, amount):
        self.interest_rate = interest_rate
        self.amount = amount

    @abstractmethod
    def increase_interest_rate(self):
        pass
