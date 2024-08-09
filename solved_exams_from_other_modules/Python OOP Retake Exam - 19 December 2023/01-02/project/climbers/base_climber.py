from abc import ABC, abstractmethod


class BaseClimber(ABC):
    STRENGTH_CLIMB_LIMIT = 0

    @abstractmethod
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    def can_climb(self):
        if self.strength >= self.STRENGTH_CLIMB_LIMIT:
            return True
        # return False

    @abstractmethod
    def climb(self, peak: object):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        conquered_peaks = ", ".join(sorted(self.conquered_peaks))
        return (f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * "
                f"Conquered peaks: {conquered_peaks} ///")
