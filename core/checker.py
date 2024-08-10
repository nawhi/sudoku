from core.model.board import SudokuBoard, subgrid_of_board


def is_solved(board: SudokuBoard) -> bool:
    if 0 in board:
        return False

    for row in board:
        if len(set(row)) != 9:
            return False

    for column in board.transpose():
        if len(set(column)) != 9:
            return False

    for i in range(3):
        for j in range(3):
            subgrid = subgrid_of_board(board, i, j)
            if len(set(subgrid.flatten())) != 9:
                return False

    return True
