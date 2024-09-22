import copy
import numpy as np

class PartialEightQueens:

    def __init__(self, n=8):
        self.n = n

        self.possible_positions = [[i for i in range(0, self.n)] for _ in range(0, self.n)]
        self.final_values = [-1] * self.n




if __name__ == "__main__":

    partial_state = PartialEightQueens()
    possible = partial_state.possible_positions
    
    print(np.matrix(possible))
