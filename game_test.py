import unittest
from random_game import *


class TestGame(unittest.TestCase):
    def test_input(self):
        result = run_random_game(5, 5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = run_random_game(5, 0, 5)
        self.assertFalse(result)

    def test_input_out_of_bounds(self):
        result = run_random_game(5, 10, 5)
        self.assertFalse(result)

    def test_input_string(self):
        result = run_random_game(5, 'string', 5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
