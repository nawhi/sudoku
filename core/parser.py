import re

import numpy as np

RE_EXTRACT_BOARD = re.compile(r"[0-9.]", re.MULTILINE)


def parse_board(raw: str):
    """
    Parse a board from a string representation.

    :param raw: The string representation of the board.
    :return: The board as a numpy array.
    """
    lines = raw.strip().split("\n")
    board = np.zeros((9, 9), dtype=int)
    numbers = RE_EXTRACT_BOARD.findall(raw)
    if len(numbers) != 81:
        raise ValueError(f"Invalid board: expected to find 81 numbers, got {len(numbers)}")

    return np.array([int(n) if n != "." else 0 for n in numbers]).reshape(9, 9)
