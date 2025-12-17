<h1>🧩 Maze Pathfinding Project</h1>

<h2>📌 Project Overview:</h2>

This project implements and compares multiple search algorithms to solve the Maze Pathfinding Problem.
The goal is to find the shortest path from a start cell to a goal cell in a grid-based maze containing obstacles.

The project demonstrates the difference between:

Uninformed Search (BFS)

Informed Search (A*)

Local Search (Hill Climbing)

<h2>🎯 Problem Description:</h2>

The maze is represented as a 2D grid:

0 → Free cell (can move)

1 → Wall (blocked)

The agent can move in four directions:

Up

Down

Left

Right

Each move has a cost of 1.

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
│   │   ├── bfs.py              # Breadth-First Search algorithm
│   │   ├── astar.py            # A* search algorithm
│   │   └── hill_climbing.py    # Hill Climbing algorithm
│   │
│   ├── problems/
│   │   └── maze.py             # Maze generation and visualization
│   │
│   ├── heuristics.py           # Heuristic functions
│   └── main.py                 # Main program entry point
│
├── results/
│   ├── performance.txt         # Performance metrics and results
│   └── analysis.txt            # Algorithm analysis and comparison
│
├── README.md                   # Project documentation
└── report.pdf                  # Final project report


