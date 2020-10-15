import math
from abc import ABC, abstractmethod
from os import system, name
from time import sleep

from Node import Node


class InformedSearch(ABC):
    name = ""
    frontier = []
    visited = []
    maze = None
    initial_node = None
    goal_states = None
    path = []
    cost = 0

    def __init__(self, name, maze, initial_node, goal_states):
        """
        搜索工具类
        :param name: 搜索器的名字
        :param maze: 迷宫
        :param initial_node: 初始节点
        :param goal_states: 目标状态
        """
        self.name = name
        self.frontier = []
        self.visited = []
        self.maze = maze
        self.initial_node = initial_node
        self.goal_states = goal_states
        self.path = []
        self.cost = 0

    def initialize(self):  # Add initial state to frontier
        """
        初始化这个分析器，清空所有缓存
        :return:
        """
        self.frontier.clear()
        self.path.clear()
        self.visited.clear()
        self.cost = 0
        self.frontier.append(self.initial_node)

    def find_possible_moves_from_node(self, node):
        """
        获取一个位置周围的所有可能的新位置
        :param node: 起始节点
        :return: 所有的可以到达的节点
        """
        accessible_nodes = []  # 可达到的位置，先用空列表占位
        cell = self.maze[node.row][node.column]  # 在迷宫中取出这个节点位置处的内容

        directions = cell["move"]  # 迷宫处的方向
        # 以下四部分基本一致，仅标注一次
        if 'w' in str(directions):  # 如果这个节点可以向西走
            adjacent = Node(node.row, node.column - 1, node)  # 下一个目标是西，也就是行不动，列减一
            distance = self.manhatten_distance(adjacent)  # 计算新位置的距离
            # 新位置的费用等于旧位置的费用加上前进一步的费用
            adjacent.cost_from_initial_node = node.cost_from_initial_node + cell["cost"]
            adjacent.distance_to_nearest_goal = distance  # 计算新位置的距离目标的最近距离
            # print('node and distance',adjacent)
            accessible_nodes.append(adjacent)  # 可达到的位置添加上这个新的位置
        if 's' in str(directions):  # 如果这个节点可以向南走
            adjacent = Node(node.row + 1, node.column, node)
            distance = self.manhatten_distance(adjacent)
            adjacent.cost_from_initial_node = node.cost_from_initial_node + cell["cost"]
            adjacent.distance_to_nearest_goal = distance
            # print('node and distance',adjacent)
            accessible_nodes.append(adjacent)
        if 'e' in str(directions):  # 如果这个节点可以向东走
            adjacent = Node(node.row, node.column + 1, node)
            distance = self.manhatten_distance(adjacent)
            adjacent.cost_from_initial_node = node.cost_from_initial_node + cell["cost"]
            adjacent.distance_to_nearest_goal = distance
            # print('node and distance',adjacent)
            accessible_nodes.append(adjacent)
        if 'n' in str(directions):  # 如果这个节点可以向北走
            adjacent = Node(node.row - 1, node.column, node)
            distance = self.manhatten_distance(adjacent)
            adjacent.cost_from_initial_node = node.cost_from_initial_node + cell["cost"]
            adjacent.distance_to_nearest_goal = distance
            # print('node and distance',adjacent)
            accessible_nodes.append(adjacent)

        return accessible_nodes

    @abstractmethod
    def add_new_nodes_to_frontier(self, nodes):
        """
        这个用于给子类进行继承，每个类自己处理
        :param nodes:
        :return:
        """
        pass

    def manhatten_distance(self, current_node):
        """
        计算某个位置到所有目标位置的最短直线距离
        :param current_node: 某个位置
        :return: 距离
        """
        manhatten_distance_goal = math.sqrt(
            (current_node.row - self.goal_states[0][0]) * (current_node.row - self.goal_states[0][0]) +
            (current_node.column - self.goal_states[0][1]) * (current_node.column - self.goal_states[0][1]))
        # print(manhatten_distance_goal, self.goal_states[0])
        for i in range(1, len(self.goal_states)):
            distance = math.sqrt(
                (current_node.row - self.goal_states[i][0]) * (current_node.row - self.goal_states[i][0]) +
                (current_node.column - self.goal_states[i][1]) * (current_node.column - self.goal_states[i][1]))
            if (manhatten_distance_goal > distance):
                manhatten_distance_goal = distance
            # print('goal state',current_node,manhatten_distance_goal, self.goal_states[i])
        # print(manhatten_distance_goal)
        return manhatten_distance_goal

    def update_path(self, current_node):  # Constructs current path and cost from scratch
        """
        指定一个位置，将路径更新为该位置到起点的路径
        :param current_node: 当前节点
        :return:
        """
        self.path.clear()  # 清空现有路径
        self.cost = 0  # 设置现有的费用为0
        current = current_node
        while current is not None:  # 遍历位置，依次记录其前一个位置，直到找到起点（起点的前一个位置为None）
            self.cost = current_node.cost_from_initial_node
            self.path.insert(0, current)
            current = current.parent

    def process_accessible_nodes(self, current_node, accessible_nodes):
        """
        处理某个节点处可以到达的节点
        对于新传入的节点，如果某个节点已经记录，则删去，否则添加入记录
        :param current_node: 当前节点
        :param accessible_nodes: 新传入的节点
        :return:
        """
        accessible_nodes = self.remove_visited_nodes(accessible_nodes)
        self.add_new_nodes_to_frontier(accessible_nodes)

    @staticmethod
    def list_contains_node(search_list, node):
        """
        判断列表中是否已存在这个节点
        :param search_list: 待搜寻的列表
        :param node: 某个节点
        :return:
        """
        if len(search_list) <= 0:  # 如果列表为空，则肯定不存在
            return False
        else:
            if isinstance(search_list[0], Node):  # 如果节点是节点类的实例，则进行处理
                for item in search_list:
                    if item.is_same(node):  # 依次比较是否是同一节点
                        return True  # 如果发现了同一节点，则返回真
            else:
                if isinstance(node, Node):  # 同理
                    for item in search_list:
                        if node.is_same(item):
                            return True
                else:
                    for item in search_list:
                        if item[0] == node[0] and item[1] == node[1]:
                            return True
            return False  # 如果前一步的循环中没有发现节点，则返回假

    @staticmethod
    def remove_node_from_list(search_list, node):
        """
        将节点从列表中删除
        :param search_list:
        :param node:
        :return:
        """
        if len(search_list) > 0:
            if isinstance(search_list[0], Node):
                for item in search_list:
                    if item.is_same(node):
                        search_list.remove(item)
                        return
            else:
                if isinstance(node, Node):
                    for item in search_list:
                        if node.is_same(item):
                            search_list.remove(item)
                            return
                else:
                    for item in search_list:
                        if item[0] == node[0] and item[1] == node[1]:
                            search_list.remove(item)
                            return

    def remove_visited_nodes(self, nodes):
        """
        将已访问过的节点删除
        :param nodes: 可能存在已访问过的节点
        :return: 过滤后的节点
        """
        counter = len(nodes) - 1
        while counter >= 0:
            if InformedSearch.list_contains_node(self.visited, nodes[counter]):
                nodes.pop(counter)
            counter -= 1
        return nodes

    def progress(self, mode):  # Gets the first state in frontier and expands it
        """
        处理
        :param mode: 模式为1则不显示迷宫，模式为2则显示迷宫
        :return:
        """
        current_node = self.frontier[0]
        # print('frontier',self.frontier[0],self.frontier[0].distance_to_nearest_goal)
        self.frontier.pop(0)  # Remove the first node from frontier
        if not InformedSearch.list_contains_node(self.visited, current_node):
            self.visited.append(current_node)
        self.update_path(current_node)
        if mode == '1' or mode == '2':
            if mode == '1':
                self.show_maze_on_console(False)
            else:
                self.show_maze_on_console(True)
        print("CURRENT:", current_node, "\nCOST:", self.cost, "\nPATH:", self.path)
        if InformedSearch.list_contains_node(self.goal_states, current_node):
            print("REACHED GOAL STATE ", current_node)
            self.path.append(current_node)
            return True
        accessible_nodes = self.find_possible_moves_from_node(current_node)
        self.process_accessible_nodes(current_node, accessible_nodes)
        print("FRONTIER:", self.frontier, "\n-----------------------------------------------------\n")

    @staticmethod
    def clear_console():
        """
        清理控制台内空
        :return:
        """
        sleep(0.5)
        if name == 'nt':  # check and make call for specific operating system
            _ = system('cls')
        else:  # for mac and linux(here, os.name is 'posix')
            _ = system('clear')

    def show_maze_on_console(self, clear):
        """
        在控制台中显示迷宫
        :param clear:
        :return:
        """
        output = '_________________\n'
        if clear:
            InformedSearch.clear_console()
        for row in range(0, len(self.maze)):
            output += "|"
            for column in range(0, len(self.maze[0])):
                if InformedSearch.list_contains_node(self.path, Node(row, column)):
                    output += "+"
                else:
                    if InformedSearch.list_contains_node(self.goal_states, Node(row, column)):
                        output += "G"
                    elif self.maze[row][column]["cost"] == 7:
                        output += "T"
                    else:
                        output += " "
                output += "|"
            output += "\n"
        output += "_________________\n"
        print(output)

    def execute(self, mode):
        """
        主函数
        :param mode: 模式为1则不显示迷宫，模式为2则显示迷宫
        :return:
        """
        self.initialize()
        print("\n", self.name, "\n_________________________________________________________________________\n")
        end = False
        while not end:  # Continue until frontier becomes empty or reach a goal state
            end = self.progress(mode)
            if len(self.frontier) == 0:
                break
        if not end:
            print("CANNOT REACH A GOAL STATE")
        print("EXPANDED NODES:", self.visited)
