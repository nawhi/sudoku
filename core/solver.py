import numpy as np

from core.checker import check_board, is_completed
from core.model.board import SudokuBoard
from core.printer import board_as_string
from core.strategies.elimination import single_cell_elimination, subgrid_elimination
from core.strategies.last_cell import last_cell_in_row, last_cell_in_column, last_cell_in_subgrid

STRATEGIES = [
    last_cell_in_row,
    last_cell_in_column,
    last_cell_in_subgrid,
    single_cell_elimination,
    subgrid_elimination
]


def all_strategies_failed(board):
    message = "\n".join([
        "Cannot solve this board with the current strategies!",
        f"Board state before failure:\n{board_as_string(board)}",
        "All strategies tried:",
        ", ".join(strategy.__name__ for strategy in STRATEGIES)
    ])
    raise NotImplementedError(message)


def board_state_and_problems(board, problems):
    problem_list = "\n".join(problems)
    board_state = board_as_string(board)
    return "\n".join([
        f"Board state:\n{board_state}",
        f"Problems:\n{problem_list}"
    ])


def incorrect_solution(board, problems):
    message = "\n".join([
        "Invalid solution!",
        board_state_and_problems(board, problems)
    ])
    raise RuntimeError(message)


def invalid_board(board, problems):
    message = "\n".join([
        "The strategy has produced an invalid board!",
        board_state_and_problems(board, problems)
    ])
    raise RuntimeError(message)


def solve(board_init: SudokuBoard) -> SudokuBoard:
    board = board_init.copy()
    while not is_completed(board):
        board_before = board.copy()
        for strategy in STRATEGIES:
            try:
                board = strategy(board)
                problems = check_board(board)
                if problems:
                    invalid_board(board, problems)
            except RuntimeError as err:
                message = "\n".join([
                    f"Strategy {strategy.__name__} failed with message: {err}",
                    "Board state before failed strategy:",
                    board_as_string(board_before)
                ])
                raise RuntimeError(message)
        if not is_completed(board) and np.array_equal(board, board_before):
            all_strategies_failed(board)

    problems = check_board(board)
    if problems:
        incorrect_solution(board, problems)

    return board
