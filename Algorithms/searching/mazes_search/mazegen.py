import random

def mazgen(height, width, obstacke_weight=0.2):

    maze = [[random.choices(['.', '%'], weights= [1-obstacke_weight, obstacke_weight])[0] \
            for _ in range(width)] for _ in range(height)]

    maze[0][0] = '.'
    maze[-1][-1] = '.'
    return maze

def print_maze(maze):
    print ("\n".join(["".join(row) for row in maze]))

def str2arrray(maze):
    return [list(row) for row in maze.split("\n")]


if __name__ == "__main__":
    random.seed(0)
    maze = mazgen(height=10, width=10)
    print_maze(maze)
