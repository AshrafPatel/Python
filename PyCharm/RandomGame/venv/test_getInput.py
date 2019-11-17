from unittest import TestCase
from sys import argv
from venv import main


class TestGetInput(TestCase):
    def test_getInput(self):
        try:
            randomLow = argv[1]
            randomHigh = argv[2]
        except Exception:
            randomLow = 2
            randomHigh = 5
        result = main.getInput(randomLow, randomHigh)
        self.assertIsInstance(result, int)

    def test_getInput2(self):
        try:
            randomLow = argv[1]
            randomHigh = argv[2]
        except Exception:
            randomLow = -4
            randomHigh = -33.6
        result = main.getInput(randomLow, randomHigh)
        self.assertIsInstance(result, int)

    def test_getInput3(self):
        try:
            randomLow = argv[1]
            randomHigh = argv[2]
        except Exception:
            randomLow = "dgsgsdgss"
            randomHigh = "sdfsdgsdsddfsdg"
        result = main.getInput(randomLow, randomHigh)
        self.assertIsInstance(result, Exception)
