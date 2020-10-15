from abc import ABC, abstractmethod
from time import sleep
from os import system, name
from Node import Node


class UninformedSearch(ABC):
    name = ""
    frontier = []
    visited = []
    maze = None
    initial_node = None
    goal_states = None
    path = []
    cost = 0

    def __init__(self, name, maze, initial_node, goal_states):
        self.name = name
        self.frontier = []
        self.visited = []
        self.maze = maze
        self.initial_node = initial_node
        self.goal_states = goal_states
        self.path = []
        self.cost = 0

    def initialize(self):  # Add initial state to frontier
        self.frontier.clear()
        self.path.clear()
        self.visited.clear()
        self.cost = 0
        self.frontier.append(self.initial_node)

    def find_possible_moves_from_node(self, node):
        accessible_nodes = []
        cell = self.maze[node.row][node.column]
        directions = cell["move"]
        if 'w' in str(directions):
            accessible_nodes.append(Node(node.row, node.column - 1, node, node.cost_from_initial_node + cell["cost"]))
        if 's' in str(directions):
            accessible_nodes.append(Node(node.row + 1, node.column, node, node.cost_from_initial_node + cell["cost"]))
        if 'e' in str(directions):
            accessible_nodes.append(Node(node.row, node.column + 1, node, node.cost_from_initial_node + cell["cost"]))
        if 'n' in str(directions):
            accessible_nodes.append(Node(node.row - 1, node.column, node, node.cost_from_initial_node + cell["cost"]))
        return accessible_nodes

    @abstractmethod
    def add_new_nodes_to_frontier(self, nodes):
        pass

    def update_path(self, current_node):  # Constructs current path and cost from scratch
        self.path.clear()
        self.cost = 0
        current = current_node
        while current is not None:
            self.cost = current_node.cost_from_initial_node
            self.path.insert(0, current)
            current = current.parent

    def process_accessible_nodes(self, current_node, accessible_nodes):
        accessible_nodes = self.remove_visited_nodes(accessible_nodes)
        self.add_new_nodes_to_frontier(accessible_nodes)

    @staticmethod
    def list_contains_node(search_list, node):
        if len(search_list) <= 0:
            return False
        else:
            if isinstance(search_list[0], Node):
                for item in search_list:
                    if item.is_same(node):
                        return True
            else:
                if isinstance(node, Node):
                    for item in search_list:
                        if node.is_same(item):
                            return True
                else:
                    for item in search_list:
                        if item[0] == node[0] and item[1] == node[1]:
                            return True
            return False

    @staticmethod
    def remove_node_from_list(search_list, node):
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
        counter = len(nodes) - 1
        while counter >= 0:
            if UninformedSearch.list_contains_node(self.visited, nodes[counter]):
                nodes.pop(counter)
            counter -= 1
        return nodes

    def progress(self, mode):  # Gets the first state in frontier and expands it
        current_node = self.frontier[0]
        self.frontier.pop(0)  # Remove the first node from frontier
        if not UninformedSearch.list_contains_node(self.visited, current_node):
            self.visited.append(current_node)
        self.update_path(current_node)
        if mode == '1' or mode == '2':
            if mode == '1':
                self.show_maze_on_console(False)
            else:
                self.show_maze_on_console(True)
        print("CURRENT:", current_node, "\nCOST:", self.cost, "\nPATH:", self.path)
        if UninformedSearch.list_contains_node(self.goal_states, current_node):
            print("REACHED GOAL STATE ", current_node)
            self.path.append(current_node)
            return True
        accessible_nodes = self.find_possible_moves_from_node(current_node)
        self.process_accessible_nodes(current_node, accessible_nodes)
        print("FRONTIER:", self.frontier, "\n-----------------------------------------------------\n")

    @staticmethod
    def clear_console():
        sleep(0.5)
        if name == 'nt':  # check and make call for specific operating system
            _ = system('cls')
        else:  # for mac and linux(here, os.name is 'posix')
            _ = system('clear')

    def show_maze_on_console(self, clear):
        output = '_________________\n'
        if clear:
            UninformedSearch.clear_console()
        for row in range(0, len(self.maze)):
            output += "|"
            for column in range(0, len(self.maze[0])):
                if UninformedSearch.list_contains_node(self.path, Node(row, column)):
                    output += "+"
                else:
                    if UninformedSearch.list_contains_node(self.goal_states, Node(row, column)):
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
