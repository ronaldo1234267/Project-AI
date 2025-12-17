<h1>🧩 Maze Pathfinding Project</h1>

<h2>📌 Project Overview:</h2>

This project implements and compares multiple search algorithms to solve the Maze Pathfinding Problem.
The goal is to find the shortest path from a start cell to a goal cell in a grid-based maze containing obstacles.

The project demonstrates the difference between:

Uninformed Search (BFS)

Informed Search (A*)

Local Search (Hill Climbing)

<h2>🎯 Problem Description</h2>

The goal is to find the shortest path from a start position to a goal position in a maze
represented as a grid.

<h3>Maze Representation</h3>

- **Free cell** → `0`
- **Wall (blocked cell)** → `1`

<h3>State Representation</h3>

- A state is represented as a coordinate pair **(x, y)**

<h3>Initial State</h3>

- The starting coordinate:  
  **start = (sx, sy)**

<h3> Goal State</h3>

- The target coordinate:  
  **goal = (gx, gy)**

<h3> Actions (Successor Function)</h3>
From any cell, the agent can move in four directions:

- Up
- Down
- Left
- Right

Moves are allowed only if:
- The cell is within the maze boundaries
- The cell is not a wall

<h3>Cost Function</h3>
- Each move has a uniform cost of **1**

<h2>🧠 Implemented Algorithms:</h2>
1️⃣ Breadth-First Search (BFS)

Explores the maze level by level

Guarantees the shortest path

High memory usage due to exploring many nodes

2️⃣ A* Search Algorithm

Uses a heuristic to guide the search

Manhattan Distance is used as the heuristic

Finds the optimal path faster than BFS

3️⃣ Hill Climbing

Greedy local search algorithm

Chooses the neighbor closest to the goal

Does NOT guarantee optimal solution

May get stuck in local minima

<h2>📐 Heuristic Functions:</h2>

The project supports multiple heuristics:

Manhattan Distance
|x1 - x2| + |y1 - y2|

Euclidean Distance

Diagonal Distance

In experiments, Manhattan Distance showed the best performance with A*.

<h2>🗂 Project Structure</h2>

The following structure shows how the project files and folders are organized:

```text
project/
├── src/
│   ├── algorithms/
│   │   ├── bfs.py
│   │   ├── astar.py
│   │   └── hill_climbing.py
│   │
│   ├── problems/
│   │   └── maze.py
│   │
│   ├── heuristics.py
│   └── main.py
│
├── results/
│   ├── performance.txt
│   └── analysis.txt
│
├── README.md
└── report.pdf
```
<h2>▶️ How to Run the Project</h2>
Make sure Python is installed

Navigate to the project directory

Run the main file:
```text
python src/main.py
```
<h2>📊 Performance Metrics</h2>

Each algorithm reports:

Path Length

Nodes Explored

Execution Time (ms)

Sample Results (50×50 Maze)
| Algorithm     | Path Length | Nodes Explored | Time (ms) | Optimal |
|---------------|------------|-----------------|-----------|---------|
| BFS           | 45         | 800             | 20        | Yes     |
| A* Search     | 45         | 150             | 5         | Yes     |
| Hill Climbing | 50         | 100             | 3         | No      |

<h2>📈 Analysis & Discussion</h2>

BFS always finds the shortest path but explores many unnecessary nodes.

A* significantly reduces the number of explored nodes using heuristics.

Hill Climbing is fast but unreliable and may fail to reach the goal.

✅ A* with Manhattan heuristic provides the best balance between efficiency and optimality.

<h2>🧾 Conclusion</h2>

This project highlights how informed search algorithms outperform uninformed ones in complex environments.
It also shows the limitations of local search methods like Hill Climbing.
