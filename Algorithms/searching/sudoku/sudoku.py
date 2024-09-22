import time
import numpy as np

def possible_values(sudoku_cell: np.ndarray, row: int, col: int, num: int) -> bool:
    """
    Check if num can be placed in sudoku_cell at (row, col).

    """

    # chevk row
    for i in range(0, 9):
        if sudoku_cell[row][i] == num:
            return False

    # check col
    for i in range(0, 9):
        if sudoku_cell[i][col] == num:
            return False

    # check square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_cell[row_start + i][col_start + j] == num:
                return False

    return True


def is_valid_initial_sudoku(sudoku: np.ndarray) -> bool:
    """
    check if the initial sudoku is invalid

    """
    for i in range(0, 9):
        row = set()
        col = set()
        square = set()

        # chevk row
        for j in range(0, 9):
            if sudoku[i][j] != 0:
                if sudoku[i][j] in row:
                    return False
                row.add(sudoku[i][j])

            # check col 
            if sudoku[j][i] != 0:
                if sudoku[j][i] in col:
                    return False
                col.add(sudoku[j][i])

            row_start = (i // 3) * 3
            col_start = (i % 3) * 3
            value = sudoku[row_start + j // 3][col_start + j % 3]

            if value != 0:
                if value in square:
                    return False
                square.add(value)

    return True


def sudoku_solver(sudoku: np.ndarray) -> np.ndarray:
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """

    solved_sudoku = np.copy(sudoku)

    # check the initial sudoku is valid
    if not is_valid_initial_sudoku(solved_sudoku):
        return -1 * np.ones_like(solved_sudoku)

    # find the empty cell (represented by 0)
    empty = None
    for row in range(0, 9):
        for col in range(0, 9):
            if solved_sudoku[row][col] == 0:
                empty = (row, col)
                break
        if empty:
            break

    if empty is None:
        return solved_sudoku

    row, col = empty

    # try to fill the empty cell with possible values
    for num in range(1, 10):
        if possible_values(solved_sudoku, row, col, num):
            solved_sudoku[row][col] = num

            result = sudoku_solver(solved_sudoku)

            if np.all(result != -1):
                return result

            solved_sudoku[row][col] = 0

    return -1 * np.ones_like(solved_sudoku)


if __name__ == "__main__":

    # Load sudokus
    sudoku = np.load("data/easy_puzzle.npy")
    print("very_easy_puzzle.npy has been loaded into the variable sudoku")

    print(
        f"sudoku.shape: {sudoku.shape}, sudoku[0].shape: {sudoku[0].shape}, sudoku.dtype: {sudoku.dtype}"
    )

    # Print the first 9x9 sudoku...
    print("First sudoku:")
    print(sudoku[1], "\n")

    start = time.process_time()
    solutions_test = sudoku_solver(sudoku[1])
    end = time.process_time()

    print("This sudoku took {} seconds to solve".format(end - start))

    print(solutions_test, "\n")

    solutions = np.load("data/easy_solution.npy")
    print(solutions[0])

    # for i in sudoku[0]:
    #     print("\n")
    #     for j, num in enumerate(i):
    #         if j == 0:
    #             print(num, end = " ")
    #         elif ((j+1) % 3 == 0) and not (j+1) == 9:
    #             print(num, end = " ")
    #             print(" | ", end = " ")
    #         else:
    #             print(num, end = " ")
