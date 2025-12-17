from problems.maze import generate_maze, print_maze
from algorithms.bfs import bfs
from algorithms.astar import a_star
from algorithms.hill_climbing import hill_climbing
from heuristics import manhattan

maze = generate_maze(20, 20)
start = (0, 0)
goal = (19, 19)

print("Running BFS...")
bfs_result = bfs(maze, start, goal)

print("Running A*...")
astar_result = a_star(maze, start, goal, manhattan)

print("Running Hill Climbing...")
hc_result = hill_climbing(maze, start, goal, manhattan)

print("\nBFS:", bfs_result)
print("A* :", astar_result)
print("HC :", hc_result)

print("\nMaze with A* Path:")
print_maze(maze, astar_result["path"])
