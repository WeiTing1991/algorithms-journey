import copy
import math

import numpy as np


class NoughtsAndCrosses:
    def __init__(self):
        self.EMPTY = " "
        self.NOUGHT = "O"
        self.CROSS = "X"
        self.DRAW = "draw"

        self.next_player = self.CROSS
        self.flip_player = {self.CROSS: self.NOUGHT, self.NOUGHT: self.CROSS}

        self.board = np.array([[self.EMPTY for _ in range(3)] for _ in range(3)])

    def valid_move(self, row: int, col: int):
        return self.board[row][col] == self.EMPTY

    def move(self, row: int, col: int):
        """Return a **copy** of the state with specified move"""
        if not self.valid_move(row, col):
            raise ValueError("Position is already taken")
        state = copy.deepcopy(self)
        state.board[row, col] = state.next_player
        state.next_player = state.flip_player[state.next_player]
        return state

    def winner(self):
        # Check the row and column are not empty
        # Check the horizontal and vertical
        for i in range(3):
            if (
                np.all(self.board[i, :] == self.board[i, 0])
                and self.board[i, 0] != self.EMPTY
            ):
                return self.board[i, 0]
            if (
                np.all(self.board[:, i] == self.board[0, i])
                and self.board[0, i] != self.EMPTY
            ):
                return self.board[0, i]

        # check diagonal
        if (
            self.EMPTY != self.board[0, 0]
            and self.board[0, 0] == self.board[1, 1]
            and self.board[1, 1] == self.board[2, 2]
        ):
            return self.board[1, 1]
        if (
            self.EMPTY != self.board[2, 0]
            and self.board[2, 0] == self.board[1, 1]
            and self.board[1, 1] == self.board[0, 2]
        ):
            return self.board[1, 1]
        if np.all(self.board != self.EMPTY):
            return self.DRAW

        return False

    def actions(self):
        row, col = np.nonzero(self.board == self.EMPTY)
        return [(r, c) for r, c in zip(row, col)]


class MinimaxAgent:
    def __init__(self, verbose=False):
        self.verbose = verbose

    def next_move(self, state=NoughtsAndCrosses()):
        player = state.next_player

        best_action = None
        best_value = -1 * math.inf
        for action in state.actions():
            new_state = state.move(action[0], action[1])
            action_value = self.get_value(new_state, player, get_min=True)
            if self.verbose:
                print(action_value, end=" ")
            if action_value > best_value:
                best_action = action
                best_value = action_value
        if self.verbose:
            print()
        return best_action

    def get_value(self, state, player, get_min):
        """ the min or max value of the state"""
        """If get_min is set to true, returns the minimum value, otherwise the maximum value"""
        other_player = state.flip_player[player]

        winner = state.winner()
        if winner == player:
            return 1
        elif winner == other_player:
            return -1
        elif winner == state.DRAW:
            return 0

        best_value = math.inf
        if not get_min:
            best_value *= -1

        for action in state.actions():
            new_state = state.move(action[0], action[1])
            action_value = self.get_value(new_state, player, get_min=not get_min)
            if (
                not get_min
                and action_value > best_value
                or get_min
                and action_value < best_value
            ):
                best_value = action_value

        return best_value

class HumanAgent:
    def next_move(self, state):
        while True:
            try:
                print("What's your next move? In format row,col")
                move = input(">")
                move = move.split(',')
                move = int(move[0]), int(move[1])
                if not state.valid_move(move[0], move[1]):
                    print("Space must be empty.")
                else:
                    return move
            except ValueError:
                print("Please enter valid space as row,col between 0,0 and 2,2")


def run_game(player1=HumanAgent(), player2=MinimaxAgent()):
    state = NoughtsAndCrosses()
    print(state.board)
    while not state.winner():
        move = player1.next_move(state)
        state = state.move(move[0], move[1])
        print(state.board)
        if state.winner() == state.CROSS:
            print("Player one wins!")
            return
        elif state.winner() == state.DRAW:
            print("It's a draw.")
            return

        move = player2.next_move(state)
        state = state.move(move[0], move[1])
        print(state.board)
        if state.winner() == state.NOUGHT:
            print("Player two wins!")
            return
        elif state.winner() == state.DRAW:
            print("It's a draw.")
            return


if __name__ == "__main__":
    run_game()

