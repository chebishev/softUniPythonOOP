from abc import abstractmethod, ABC


class BaseDuck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class Walkable(ABC):
    @staticmethod
    @abstractmethod
    def walk():
        pass


class Flyable(ABC):
    @staticmethod
    @abstractmethod
    def fly():
        pass


class RubberDuck(BaseDuck):
    @staticmethod
    def quack():
        return "Squeak"


class RobotDuck(BaseDuck, Walkable, Flyable):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


class Duck(BaseDuck, Walkable, Flyable):

    @staticmethod
    def quack():
        return "Quack"

    @staticmethod
    def walk():
        return "Walk"

    @staticmethod
    def fly():
        return "Fly"
