import math
import time
import numpy as np
from minimax_search import NoughtsAndCrosses


class ABMinimaxAgent:
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

    def get_value(self, state, player, get_min, alpha=-math.inf, beta=math.inf):
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
            action_value = self.get_value(new_state, player, get_min=not get_min, alpha=alpha, beta=beta)
            
            if not get_min:
                alpha = max(alpha, action_value)
                if action_value >= beta:
                    return action_value
            else:
                beta = min(beta, action_value)
                if action_value <= alpha:
                    return action_value

            if not get_min and action_value > best_value \
                    or get_min and action_value < best_value:
                best_value = action_value

        return best_value
    
def run_game(player1, player2):
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
    start_time = time.process_time()
    run_game(player1=ABMinimaxAgent(), player2=ABMinimaxAgent())
    end_time = time.process_time()

    print(f"Time taken: {end_time - start_time} seconds")
