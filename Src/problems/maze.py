import random

def generate_maze(rows, cols, obstacle_prob=0.3):
    maze = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if random.random() < obstacle_prob:
                maze[i][j] = 1

    return maze

