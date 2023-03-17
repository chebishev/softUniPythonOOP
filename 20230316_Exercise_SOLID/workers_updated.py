from abc import ABC, abstractmethod
import time


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class BaseWorker:
    pass


class Worker(BaseWorker, Workable, Eatable):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(BaseWorker, Workable, Eatable):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), f"`worker` must be of type {BaseWorker}"

        self.worker = worker

    def manage(self):
        self.worker.work()

    def lunch_break(self):
        if isinstance(self.worker, Eatable):
            self.worker.eat()


class Robot(BaseWorker, Workable):

    def work(self):
        print("I'm a robot. I'm working....")


manager = Manager()
manager.set_worker(Worker())
manager.manage()
manager.lunch_break()

manager.set_worker(SuperWorker())
manager.manage()
manager.lunch_break()

manager.set_worker(Robot())
manager.manage()
manager.lunch_break()
