# DijstraAlgorithm
***
 ## Program that finds the shortest path in the maze
 
#### Technologies
Python 
Streamlit
HTML
CSS

 
 [What is the dijsktra algorithms?](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
 
 [What is the shortest path algorithms?](https://en.wikipedia.org/wiki/Shortest_path_problem)
 

| Dijstra Algorithm  | A*Algorithm   |
| ----------------- |:-------------:|
| Dijkstra's just explore all possible paths.         | A* uses heuristics to optimize the search.  |
| uninformed search algorithm        | informed search algorithm      |
| Algorithm is an algorithm that finds the shortest path between nodes A and B in a directed graph with non-negative edge weights.  | The A* algorithm is based on heuristics for navigating the search, but unlike many similar algorithms with this base (for example Best Search Algorithm), it is both complete and (under certain conditions) optimal      |
| The complexity of this algorithm is O(|E|+|V|log|V|), where |E| represents the number of edges, while |V| represents the number of nodes. | One major practical drawback is its O(b^d) space complexity, as it stores all generated nodes in memory.  |
| Dijkstra has a visited set and distance values to determine which node to go to next. Here we have one cost function f(x)=g(x) where we focus on finding the real cost value from the source to each node.| A* search has two cost functions f(x) = g(x) + h(x) where g(x) is the same as Dijkstra and h(x) is the approximate cost from node x to the goal node.     |
