# Graph Theory - Minimum Spanning Tree (MST) Group Homework

## 1. Identity
**Informatics ITS Graph Theory class Group [Your Group Number]**

* [Member 1 Name] - [NRP/Student ID]
* [Member 2 Name] - [NRP/Student ID]
* [Member 3 Name] - [NRP/Student ID]
* [Member 4 Name] - [NRP/Student ID]

---

## 2. Short Explanation About Algorithms
Our group implemented three distinct algorithms to find the Minimum Spanning Tree (MST) and adapt to network failures:

* **Prim's Algorithm:** A greedy algorithm that builds the MST one vertex at a time. It maintains a set of visited vertices and repeatedly selects the lowest-weight edge that connects a visited node to an unvisited node until all active nodes are connected.
* **Kruskal's Algorithm:** A greedy algorithm that sorts all edges by weight in ascending order. It iterates through the sorted edges and adds them to the MST, using a Disjoint Set (Union-Find) data structure to ensure no cycles are formed.
* **Borůvka's Algorithm:** A component-based algorithm that initializes each node as its own distinct tree. In each phase, it simultaneously finds the minimum-weight edge connecting each tree to another, merging them until only a single spanning tree remains.

---

## 3. Prerequisites to Run the Code
* A standard C compiler (e.g., `gcc`).
* Standard C libraries: `<stdio.h>`, `<stdlib.h>`, `<stdbool.h>`, `<limits.h>`.
* A terminal or command-line interface.

---

## 4. Instructions to Run the Code
You can quickly compile and run the source files directly from your terminal.

### Option A: Manual Compilation
1. Open your terminal and navigate to the project directory.
2. Compile the files using `gcc`:
   * `gcc prim.c -o prim`
   * `gcc kruskal.c -o kruskal`
   * `gcc boruvka.c -o boruvka`
3. Execute the compiled binaries:
   * `./prim`
   * `./kruskal`
   * `./boruvka`

### Option B: Automated Execution
To streamline the process, you can create a quick `run.sh` script in your project root:

```bash
#!/bin/bash
echo "Compiling..."
gcc prim.c -o prim
gcc kruskal.c -o kruskal
gcc boruvka.c -o boruvka

echo "--- Running Prim's ---"
./prim

echo "--- Running Kruskal's ---"
./kruskal

echo "--- Running Boruvka's ---"
./boruvka
