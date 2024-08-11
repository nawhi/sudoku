from typing import List

from core.model.board import SudokuBoard


def to_threes(lst: List[int]) -> List[List[int]]:
    return [lst[i:i + 3] for i in range(0, len(lst), 3)]


def cells_as_string(cells: List[int]) -> str:
    return " ".join([f"{cell or '.'}" for cell in cells])


def row_as_string(row: List[int]) -> str:
    return f"│ {cells_as_string(row[:3])} │ {cells_as_string(row[3:6])} │ {cells_as_string(row[6:9])} │"


def board_as_string(board: SudokuBoard) -> str:
    header = "┌───────┬───────┬───────┐"
    footer = "└───────┴───────┴───────┘"
    separator = "├───────┼───────┼───────┤"

    rows = board.tolist()

    rows = [
        header,
        row_as_string(rows[0]),
        row_as_string(rows[1]),
        row_as_string(rows[2]),
        separator,
        row_as_string(rows[3]),
        row_as_string(rows[4]),
        row_as_string(rows[5]),
        separator,
        row_as_string(rows[6]),
        row_as_string(rows[7]),
        row_as_string(rows[8]),
        footer
    ]

    return "\n".join(rows)
