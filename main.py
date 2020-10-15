"""
这个文件是主程序。
"""

import json

from AStar import AStar
from Node import Node


def main(file, mode):
    with open(file) as maze_file:
        maze_data = json.load(maze_file)  # 从文件中加载迷宫
        maze = maze_data["maze"]  # 取出迷宫数据
        initial_state = maze_data["initial_state"]  # 取出初始状态
        initial_state = Node(initial_state[0], initial_state[1])  # 将初始状态转换为一个Node对象
        goal_states = maze_data["goal_states"]  # 取出目标状态

        # dfs = DFS("DEPTH-FIRST SEARCH", maze, initial_state, goal_states)
        # dfs.execute(mode)

        # bfs = BFS("BREADTH-FIRST SEARCH", maze, initial_state, goal_states)
        # bfs.execute(mode)

        # ucs = UCS("UNIFORM-COST SEARCH", maze, initial_state, goal_states)
        # ucs.execute(mode)

        # gbfs = GreedyBestFirstSearch("Greedy Best First Search", maze, initial_state, goal_states)
        # gbfs.execute(mode)

        # ***************************HOMEWORK***********************************
        astar = AStar("A Star Search", maze, initial_state, goal_states)  # 创建搜索器实例
        astar.execute(mode)  # 按给定的模式执行搜索


if __name__ == '__main__':
    file_input = "maze.json"
    exec_mode = '1'
    main(file_input, exec_mode)
