import time

def hill_climbing(maze, start, goal, heuristic):
    current = start
    visited = set([current])
    path = [current]
    nodes_explored = 0

    start_time = time.time()

    while current != goal:
        neighbors = []

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    neighbors.append((nx, ny))

        if not neighbors:
            break

        current = min(neighbors, key=lambda x: heuristic(x, goal))
        visited.add(current)
        path.append(current)
        nodes_explored += 1

    end_time = time.time()

    return {
        "path": path,
        "path_length": len(path),
        "nodes_explored": nodes_explored,
        "time_ms": (end_time - start_time) * 1000
    }
