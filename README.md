The program input a maze file the format of which will be determined by yourself. 
The letter “S” denotes the starting square, the letter “G” denotes one or more goal squares and the letter “T” denotes the squares with trap. 

The cost of each move is one point, however, when the agent moves in a trap square, the cost of the move will increase by 6 (i.e. the total cost of the move will be 7 instead of 1).
For every search method, the order of node expansion should be East, South, West, North. 

 
For the above maze and for each search method, program displays
i.	The cost of the solution found.
ii.	The solution path itself. 
iii. The list of expanded nodes.


a.	For Greedy Best First Search and A* Heuristic Search, you should use city block distance (Manhattan distance) as an admissible heuristic or a more informed admissible heuristic.
