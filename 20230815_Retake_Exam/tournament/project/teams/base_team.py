from abc import ABC, abstractmethod
from math import floor


class BaseTeam(ABC):
    ADVANTAGE = 0

    @abstractmethod
    def __init__(self, name, country, advantage, budget):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    def win(self):
        self.wins += 1
        self.advantage += self.ADVANTAGE

    def result(self):
        return self.advantage + sum(equipment.protection for equipment in self.equipment)

    def get_statistics(self):
        total_price_of_equipment = sum(p.price for p in self.equipment)
        avg_team_protection = sum(p.protection for p in self.equipment) / len(self.equipment) if len(self.equipment) > 0 else 0

        return f"Name: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Advantage: {self.advantage} points\n" \
               f"Budget: {self.budget:.2f}EUR\n" \
               f"Wins: {self.wins}\n" \
               f"Total Equipment Price: {total_price_of_equipment:.2f}\n" \
               f"Average Protection: {floor(avg_team_protection)}"
