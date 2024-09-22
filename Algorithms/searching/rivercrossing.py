class Node:
    def __init__(self, m_wrong_side=0, c_wrong_side=0, boat_wrong_side=0, state=None, parent=None, action=None):

        self.m_wrong_side = m_wrong_side
        self.c_wrong_side = c_wrong_side
        self.boat_wrong_side = boat_wrong_side

        if state is None:
            self.state = (m_wrong_side, c_wrong_side, boat_wrong_side)
        else:
            self.state = state

        self.parent = parent
        self.action = action

    def is_goal_state(self):
        return self.state == (0, 0, 0)

    def get_child_node(self, action):

        if self.state[2] == 1:
            new_state = (self.state[0]-action[0],
                         self.state[1]-action[1],
                         self.state[2]-action[2])
        else:
            new_state = (self.state[0]+action[0],
                         self.state[1]+action[1],
                         self.state[2]+action[2])

        return Node(state=new_state, parent=self, action=action)

    def is_valid_state(self):
        m = self.state[0]
        c = self.state[1]

        if m< 0 or c< 0:
            return False
        if (m > 0 and m < c):
            return False
        return True

class Game:
    def __init__(self):
        self.initial_state = Node(m_wrong_side=3, c_wrong_side=3, boat_wrong_side=1)
        self.actions = [(1, 0, 1), (2, 0, 1), (0, 1, 1), (0, 2, 1), (1, 1, 1)]  # Possible actions

    def breadth_first_search(self):
        state = self.initial_state
        frontier = [state]
        explored = set()

        while frontier:
            current_state = frontier.pop(0)

            if current_state.is_goal_state():
                return current_state

            explored.add(current_state.state)

            for action in self.actions:
                child_node = current_state.get_child_node(action)
                if child_node.is_valid_state() and child_node.state not in explored:
                    frontier.append(child_node)

        return None  # No solution found


g = Game()
goal_node = g.breadth_first_search()

if goal_node:
    print("Goal state found!")
else:
    print("No solution found.")
