import unittest

from core.checker import is_solved
from core.model.board import SudokuBoard
from core.parser import parse_board
from core.solver import solve
from test.util import SudokuTestCase
from test.examples import PUZZLE_EASY, PUZZLE_MEDIUM, PUZZLE_HARD

import os


def can_solve(puzzle: str):
    return is_solved(solve(parse_board(puzzle)))


def load_from_digit_string(line: str) -> SudokuBoard:
    """ Loads from 81 digit string into SudokuBoard"""
    return parse_board("".join(line.split()))


def load_qqwing_examples(level: str):
    path = os.path.join("resources", f"qqwing_{level}.sdm")
    with open(path) as f:
        return [parse_board(line) for line in f.readlines()]


class TestSolver(SudokuTestCase):
    def test_solves_single_easy(self):
        self.assertTrue(can_solve(PUZZLE_EASY))

    # @unittest.skip("WIP")
    def test_solves_single_medium(self):
        self.assertTrue(can_solve(PUZZLE_MEDIUM))

    @unittest.skip("WIP")
    def test_solves_single_hard(self):
        self.assertTrue(can_solve(PUZZLE_HARD))

    @unittest.skip("WIP - currently 1,453 of 4,001")
    def test_solves_all_generated_examples(self):
        for level in ["simple", "easy", "intermediate", "expert"]:
            for i, example in enumerate(load_qqwing_examples(level)):
                with self.subTest(f"qqwing {level} line {i}"):
                    self.assertTrue(is_solved(solve(example)))
