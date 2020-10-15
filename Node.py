class Node:
    row = -1
    column = -1
    parent = None
    cost_from_initial_node = 0
    distance_to_nearest_goal = 0

    def __init__(self, row, column, parent=None, cost=0, distance_to_nearest_goal=0):
        self.row = row
        self.column = column
        self.parent = parent
        self.cost_from_initial_node = cost
        self.distance_to_nearest_goal = distance_to_nearest_goal
        

    def is_same(self, compare):
        if isinstance(compare, Node):
            return compare.row == self.row and compare.column == self.column
        else:
            return compare[0] == self.row and compare[1] == self.column

    def __repr__(self):
        return "[" + str(self.row) + "," + str(self.column) + "]"
