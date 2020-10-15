这个程序输入一个迷宫文件，这个迷宫文件的格式由您自己进行定义。
S表示迷宫的起点方块，G表示迷宫的目标方块，T表示陷阱方块。

The program input a maze file the format of which will be determined by yourself. 
The letter “S” denotes the starting square, 
the letter “G” denotes one or more goal squares and the letter “T” denotes the squares with trap. 

每一次移动的费用为1，然而，当特工移动至一个陷阱方块里时，会花费额外6的费用。
对于每一个搜索方法，前进的顺序应该是东、南、西、北。

The cost of each move is one point, however, when the agent moves in a trap square, the cost of the move will increase by 6 (i.e. the total cost of the move will be 7 instead of 1).
For every search method, the order of node expansion should be East, South, West, North. 

对于上面的迷宫和搜索方法，程序显示以下内容：

1. 解决方案的费用。
2. 解决方案的路径本身。
1. 扩展的节点的列表。
 
For the above maze and for each search method, program displays
i.	The cost of the solution found.
ii.	The solution path itself. 
iii. The list of expanded nodes.

对于贪心最佳第一次搜索和A*启发式搜索，你应该使用城市方块距离（曼哈顿距离）作为一个可容许的启发，或者更明智的启发。

a.	For Greedy Best First Search and A* Heuristic Search, 
you should use city block distance (Manhattan distance) 
as an admissible heuristic or a more informed admissible heuristic.
