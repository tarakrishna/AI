<h1> CIA-1</h1>

The following algorithms are prsent in the CIA-1 file:
1) British museam serach
2) Depth first search
3) Breadth first search
4) Hill climbing
5) Beam Search
6) Oracle
7) Branch and bound algorithm
8) Branch and bound algorithm (greedy)
9) Branch and bound algorithm (greedy and exit)
10) Branch and bound algorithm (greedy and heuristics)
11) Branch and bound algorithm (heuristics)
12) A* algorithm
<br>
The example used for each of the algorithm is:

![aimapping](https://github.com/user-attachments/assets/7fbb41fd-e28f-4592-877f-c5168edf7430)

<br>
The following is graph and heuristics is made based on the example preent in the above image:<br>
<h3>Graph structure</h3>
graph = {<br>
    'S': {'A': 3, 'B': 5},<br>
    'A': {'B': 4, 'D': 3},<br>
    'B': {'C': 4},<br>
    'C': {'E': 6},<br>
    'D': {'G': 5},<br>
    'E': {},<br>
    'G': {}<br>
}<br>

<h3>Heuristic values</h3>
heuristics = {<br>
    'S': 10,<br>
    'A': 7,<br>
    'B': 6,<br>
    'C': 4,<br>
    'D': 3,<br>
    'E': 2,<br>
    'G': 0<br>
}<br>

<br>
<h1> CIA-2</h1>
The CIA-2 file consists of the alpha-beta pruning code in python.
The follwoing example is used to run the code:

![alphabeta](https://github.com/user-attachments/assets/13def71d-8b22-45dc-91a3-81ec5cca5989)

