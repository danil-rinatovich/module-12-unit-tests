import unittest
from tests_12_1 import Runner
from tests_12_2 import Runner
from tests_12_2 import Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
            runner = Runner('Danil')
            for i in range(0, 10):
                runner.walk()
            self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
            runner = Runner('Danil')
            for i in range(0, 10):
                runner.run()
            self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        first_runner = Runner('Danil')
        second_runner = Runner('Danil')
        for i in range(0, 10):
            first_runner.run()
            first_runner.walk()
            second_runner.run()
            second_runner.walk()

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.usain_runner = Runner('Усэйн', 10)
        self.andrey_runner = Runner('Андрей', 9)
        self.nick_runner = Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for k, v in self.all_results.items():
            print(f'{k}: {v}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain_runner, self.nick_runner)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())].name, self.nick_runner)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey_runner, self.nick_runner)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())].name, self.nick_runner)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain_runner, self.andrey_runner, self.nick_runner)
        result = tournament.start()
        self.assertTrue(result[max(result.keys())].name, self.nick_runner)