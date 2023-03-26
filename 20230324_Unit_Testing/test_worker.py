class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker('John', 1000, 100)

    def test_correct_variable_name(self):
        result = self.worker.name
        self.assertEqual(result, 'John')

    def test_correct_variable_salary(self):
        result = self.worker.salary
        self.assertEqual(result, 1000)

    def test_correct_variable_energy(self):
        worker = Worker('John', 1000, 100)
        self.assertEqual(worker.energy, 100)

    def test_energy_incrementing(self):
        worker = Worker('John', 1000, 100)
        worker.rest()
        self.assertEqual(worker.energy, 101)

    def test_negative_energy_exception(self):
        with self.assertRaises(Exception) as e:
            worker = Worker('John', 1000, 0)
            worker.work()
        self.assertEqual(str(e.exception), 'Not enough energy.')

    def test_increasing_of_money_after_work(self):
        worker = Worker('John', 1000, 100)
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_energy_decreasing_after_work(self):
        worker = Worker('John', 1000, 100)
        worker.work()
        self.assertEqual(worker.energy, 99)

    def test_get_info_method(self):
        worker = Worker("Atanas", 1200, 100)
        result = worker.get_info()
        self.assertEqual(result, "Atanas has saved 0 money.")


if __name__ == '__main__':
    unittest.main()
