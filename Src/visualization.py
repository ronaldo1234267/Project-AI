import matplotlib.pyplot as plt
import numpy as np

def draw_maze(maze, path=None, title="Maze"):
    maze_array = np.array(maze)

    plt.figure(figsize=(6, 6))
    plt.imshow(maze_array, cmap="gray_r")

    if path:
        y = [p[1] for p in path]
        x = [p[0] for p in path]
        plt.plot(y, x)

        # Start & Goal
        plt.scatter(y[0], x[0], marker='o')
        plt.scatter(y[-1], x[-1], marker='x')

    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()
