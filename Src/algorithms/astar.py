import heapq
import time

def a_star(maze, start, goal, heuristic):
    rows, cols = len(maze), len(maze[0])
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {}
    nodes_explored = 0

    start_time = time.time()

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == goal:
            break

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = current[0] + dx, current[1] + dy
            neighbor = (nx, ny)

            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] == 0:
                    tentative_g = g_cost[current] + 1
                    if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                        g_cost[neighbor] = tentative_g
                        f = tentative_g + heuristic(neighbor, goal)
                        heapq.heappush(open_list, (f, neighbor))
                        parent[neighbor] = current

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