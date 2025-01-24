import unittest
import random

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run_1 = Runner('Dima')
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50, 'Walk test - OK')

    def test_run(self):
        run_1 = Runner('Dima')
        for _ in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 100, 'Run test - OK')

    @unittest.skip('Демонстрация ошибки')
    def test_run_with_err(self):
        # Специально сделаем тест с ошибкой. Надо исключить его, тогда норм
        run_1 = Runner('Dima')
        for _ in range(10):
            run_1.run()
        self.assertEqual(run_1.distance, 10, 'Run test - OK')

    def test_challenge(self):
        run_1 = Runner('Dima')
        run_2 = Runner('Sasha')
        # Далее запускаем 10 раз каждого бегуна с рандомным выбором бега/ходьбы
        for _ in range(10):
            if random.randint(0,1):
                run_1.walk()
            else:
                run_1.run()
        for _ in range(10):
            if random.randint(0,1):
                run_2.walk()
            else:
                run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)




if __name__ == '__main__':
    unittest.main(verbosity=5)