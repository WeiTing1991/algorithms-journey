import numpy as np
import time

def solve_sudoku(board):
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    empty_cells = []

    # Initialize bitmask
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0:
                bit = 1 << (num - 1)
                rows[r] |= bit
                cols[c] |= bit
                boxes[(r // 3) * 3 + (c // 3)] |= bit
            else:
                empty_cells.append((r, c))

    def backtrack(index):
        if index == len(empty_cells):
            return True
        r, c = empty_cells[index]
        for num in range(1, 10):
            bit = 1 << (num - 1)
            if not (rows[r] & bit) and not (cols[c] & bit) and not (boxes[(r // 3) * 3 + (c // 3)] & bit):
                # Place number
                rows[r] |= bit
                cols[c] |= bit
                boxes[(r // 3) * 3 + (c // 3)] |= bit
                board[r][c] = num
                if backtrack(index + 1):
                    return True
                # Remove number
                rows[r] ^= bit
                cols[c] ^= bit
                boxes[(r // 3) * 3 + (c // 3)] ^= bit
                board[r][c] = 0
        return False

    backtrack(0)

# Example usage
board = np.array([
    [0, 0, 2, 0, 6, 0, 0, 3, 0],
    [0, 5, 0, 0, 1, 0, 0, 0, 7],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 8, 0, 0, 0],
    [5, 0, 4, 1, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 9, 0, 0, 0, 2, 5, 0, 8],
    [0, 0, 0, 0, 5, 0, 0, 6, 0]
])

start = time.process_time()
solve_sudoku(board)
end = time.process_time()
print(board)


