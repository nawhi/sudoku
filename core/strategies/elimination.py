import numpy as np

from core.model.board import SudokuBoard, subgrid_of_board, subgrids_of_board


def single_cell_elimination(board: SudokuBoard) -> SudokuBoard:
    """ Fills in a cell's value if there is only one possibility left """
    it = np.nditer(board, flags=['multi_index'])
    for val in it:
        if val != 0:
            continue
        x, y = it.multi_index
        candidates = set(range(1, 10))

        row = board[x, :]
        candidates -= set(row)

        if len(candidates) == 1:
            board[x, y] = candidates.pop()
            continue

        col = board[:, y]
        candidates -= set(col)

        if len(candidates) == 1:
            board[x, y] = candidates.pop()
            continue

        subgrid = subgrid_of_board(board, x // 3, y // 3)
        candidates -= set(subgrid.flatten())

        if len(candidates) == 1:
            board[x, y] = candidates.pop()
            continue

    return board


def subgrid_elimination(board: SudokuBoard) -> SudokuBoard:
    """ Fills in any values in a subgrid if there is only one possibility """
    for subgrid_x in range(3):
        for subgrid_y in range(3):
            offset_x, offset_y = subgrid_x * 3, subgrid_y * 3
            subgrid = subgrid_of_board(board, subgrid_x, subgrid_y)
            empty_locations = np.argwhere(subgrid == 0)

            missing_nums = set(range(1, 10)) - set(subgrid.flatten())

            for num in missing_nums:
                possible_locations = []
                for local_x, local_y in empty_locations:
                    global_x, global_y = local_x + offset_x, local_y + offset_y
                    is_possible = num not in board[global_x, :] and num not in board[:, global_y]
                    if is_possible:
                        possible_locations.append((local_x, local_y))

                if len(possible_locations) == 1:
                    x, y = possible_locations[0]
                    board[x + offset_x, y + offset_y] = num

    return board


def row_elimination(board: SudokuBoard) -> SudokuBoard:
    print("Row elimination strategy not implemented yet")
    return board


def column_elimination(board: SudokuBoard) -> SudokuBoard:
    print("Column elimination strategy not implemented yet")
    return board
