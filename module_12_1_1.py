import Runner
import unittest
import time
from datetime import datetime

time_start = datetime.now()
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('Иван')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        run = runner.Runner('Фёдор')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        walker2 = runner.Runner('Алиса')
        run2 = runner.Runner('Даниил')
        for i in range(10):
            walker2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walker2.distance)
time_stop = datetime.now()
time_of_line = time_stop - time_start
print(f'Запуск трёх тестов за: {time_of_line} секунд')