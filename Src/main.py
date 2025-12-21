
from problems.maze import generate_maze
from algorithms.bfs import bfs
from algorithms.astar import a_star
from algorithms.hill_climbing import hill_climbing
from heuristics import manhattan
from visualization import draw_maze

def print_result(name, result):
    if result is None or "path" not in result:
        print(f"{name}: No path found")
        return

    print(f"\n{name} Results")
    print("-" * 30)
    print(f"Path length    : {result['path_length']}")
    print(f"Nodes explored : {result['nodes_explored']}")
    print(f"Time (ms)      : {result['time_ms']:.2f}")

# =========================

maze = generate_maze(20, 20)
start = (0, 0)
goal = (19, 19)

print("\nRunning BFS...")
bfs_result = bfs(maze, start, goal)

print("Running A*...")
astar_result = a_star(maze, start, goal, manhattan)

print("Running Hill Climbing...")
hc_result = hill_climbing(maze, start, goal, manhattan)

# ===== Print Results =====

print_result("BFS", bfs_result)
print_result("A*", astar_result)
print_result("Hill Climbing", hc_result)

# ===== Visualization =====

if bfs_result and "path" in bfs_result:
    draw_maze(maze, bfs_result["path"], "BFS Path")

if astar_result and "path" in astar_result:
    draw_maze(maze, astar_result["path"], "A* Path")

if hc_result and "path" in hc_result:
    draw_maze(maze, hc_result["path"], "Hill Climbing Path")


