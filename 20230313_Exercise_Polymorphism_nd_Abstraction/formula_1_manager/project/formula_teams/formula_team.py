from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget):
        self.budget = budget
        
    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @property
    @abstractmethod
    def sponsors(self) -> dict:
        pass

    @staticmethod
    @abstractmethod
    def expenses():
        pass

    def calculate_revenue_after_race(self, race_pos):
        money_from_sponsors = 0
        for sponsor, value in self.sponsors.items():
            for position in value:
                if race_pos <= position:
                    money_from_sponsors += value[position]
                    break

        revenue = money_from_sponsors - self.expenses()
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
