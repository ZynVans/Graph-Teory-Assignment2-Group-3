# Graph Theory - Minimum Spanning Tree (MST) Group Homework

## 1. Identity
**Informatics ITS Graph Theory class Group 3**

* Dzulfiqar Rafi'ussunnah - 5025251011
* Padhang Abiyu Fikri - 5025251014
* Aditya Lingga Mardika - 5025251158
* Muhammad Faris Alfarrel - 5025251002

---

## 2. Short Explanation About Algorithms
Our group implemented three distinct algorithms to find the Minimum Spanning Tree (MST) and adapt to network failures:

* **Prim's Algorithm:** A greedy algorithm that builds the MST one vertex at a time. It maintains a set of visited vertices and repeatedly selects the lowest-weight edge that connects a visited node to an unvisited node until all active nodes are connected.
* **Kruskal's Algorithm:** A greedy algorithm that sorts all edges by weight in ascending order. It iterates through the sorted edges and adds them to the MST, using a Disjoint Set (Union-Find) data structure to ensure no cycles are formed.
* **Borůvka's Algorithm:** A component-based algorithm that initializes each node as its own distinct tree. In each phase, it simultaneously finds the minimum-weight edge connecting each tree to another, merging them until only a single spanning tree remains.
---

## 3. Prerequisites to Run the Code
* Python 3.x installed on your system.
* A terminal or command-line interface.
* No external libraries are required (only Python standard libraries).
* Install IDE you prefer and run on it.

---

## 4. Instructions to Run the Code
You can run the Python scripts directly from your terminal.

---

## 4. Result of Sample Run
* Kruskal Algorithm Result
<img width="322" height="400" alt="image" src="https://github.com/user-attachments/assets/64879a10-b5f1-47f6-8e8f-2f20c99d1d54" />

