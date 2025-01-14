import unittest
from pprint import pprint
from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
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

    def test_usain_and_nick(self):
        tournament = Tournament(90, [self.usain_runner, self.nick_runner])
        tournament.start()
        self.assertTrue(tournament.participants[-1].name == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, [self.andrey_runner, self.nick_runner])
        tournament.start()
        self.assertTrue(tournament.participants[-1].name == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, [self.usain_runner, self.andrey_runner, self.nick_runner])
        tournament.start()
        self.assertTrue(tournament.participants[-1].name == "Ник")


if __name__ == '__main__':
    unittest.main()