from abc import ABC, abstractmethod


class BaseDiver(ABC):
    INITIAL_OXYGEN = 0
    REDUCE_PERCENT = 0

    @abstractmethod
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0.0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    def miss(self, time_to_catch):
        value_to_reduce = time_to_catch * self.REDUCE_PERCENT
        result = self.oxygen_level - value_to_reduce
        if result <= 0:
            result = 0
            self.has_health_issue = True
        self.oxygen_level = round(result)

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN

    def hit(self, fish):
        if self.oxygen_level >= fish.time_to_catch:
            self.oxygen_level -= fish.time_to_catch
            if self.oxygen_level == 0:
                self.has_health_issue = True
            self.catch.append(fish)
            self.competition_points += fish.points
        else:
            self.oxygen_level = 0
            self.has_health_issue = True

    def update_health_status(self):
        if self.has_health_issue:
            self.has_health_issue = False
        else:
            self.has_health_issue = True

    def __str__(self):
        return f"{self.__class__.__name__}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points:.1f}]"
