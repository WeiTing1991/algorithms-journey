import sys

sys.path.append("/")
from hanoi import HanoiState

def depth_first_search():
    state = HanoiState()
    fontier = [state]
    explored = []
    generated = 0

    current_state = fontier.pop(0)

    while not current_state.is_goal_state():
        explored.append(current_state)
        actions = current_state.possible_actions()
        for action in actions:
            generated += 1
            new_state = current_state.next_state(action[0], action[1])
            if new_state not in explored and new_state not in fontier:
                fontier.append(new_state)

        if len(fontier) == 0:
            print("No solution found")
            return

        current_state = fontier.pop()

    print("Solurion found")
    print(f"Explored {len(explored)} states")
    print(f"Generated {generated} states")
    print()

    final_path = []
    while current_state.parent is not None:
        final_path.append(current_state)
        current_state = current_state.parent

    final_path.append(current_state)

    for state in reversed(final_path):
        if state.action is not None:
            print(f"Move disk from peg {state.action[0]} to {state.action[1]}")
        print(state)
    print(f"Total {len(final_path)-1} steps")


depth_first_search()

