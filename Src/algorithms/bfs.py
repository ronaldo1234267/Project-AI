from collections import deque
import time

def bfs(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    parent = {}
    nodes_explored = 0

    start_time = time.time()

    while queue:
        current = queue.popleft()
        nodes_explored += 1

        if current == goal:
            break

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = current
                    queue.append((nx, ny))

    end_time = time.time()

    # Reconstruct path
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = parent.get(cur)
        if cur is None:
            return None
    path.append(start)
    path.reverse()

    return {
        "path": path,
        "path_length": len(path),
        "nodes_explored": nodes_explored,
        "time_ms": (end_time - start_time) * 1000
    }