
# Longest Path in a Weighted Directed Acyclic Graph (DAG)

## Overview
This repository contains a Python solution to find the longest path in a Weighted Directed Acyclic Graph (DAG).

## Problem Statement
Given a Directed Acyclic Graph (DAG) represented as an adjacency list, the task is to find the longest path in the graph starting from any node.

## Example
Input:
```
graph = [ [(1, 3), (2, 2)], [(3, 4)], [(3, 1)], [] ]
```
Output: `7`

Explanation: The longest path is from node `0 -> 1 -> 3` with a total weight of `3 + 4 = 7`.

## Files
- `main.py`: Contains the `longest_path` function and a sample graph execution.
- `test_main.py`: Contains unit tests for the `longest_path` function.

## How to Run
Clone the repository:
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

Run the main script:
```sh
python main.py
```

Run the tests:
```sh
python -m unittest test_main.py
```

