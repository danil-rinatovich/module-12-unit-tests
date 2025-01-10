import unittest
from unittest import TestCase


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


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Danil')
        for i in range(0, 10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('Danil')
        for i in range(0, 10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        first_runner = Runner('Danil')
        second_runner = Runner('Danil')
        for i in range(0, 10):
            first_runner.run()
            first_runner.walk()
            second_runner.run()
            second_runner.walk()


if __name__ == '__main__':
    unittest.main()