from abc import ABC, abstractmethod


class Animal(ABC):

    @staticmethod
    @abstractmethod
    def make_sound():
        pass


class Cat(Animal):

    @staticmethod
    def make_sound():
        print("meow")


class Dog(Animal):

    @staticmethod
    def make_sound():
        print("woof-woof")


class Hen(Animal):

    @staticmethod
    def make_sound():
        print("cluck-cluck")


def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()


animals = [Cat(), Dog(), Hen()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
