from horse_racings.project import Person
from horse_racings.project import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
