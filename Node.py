class Node:
    """
    这个类看起来是要定义一个数据类型，用来记录该节点的结构
    """
    row = -1  # 设置行为-1作为默认值，可以理解为是空值
    column = -1  # 设置列为-1作为默认值，可以理解为空值
    parent = None  # 父节点
    cost_from_initial_node = 0  # 从初始节点查过来的费用，这个费用应该可以理解为距离初始节点的距离
    distance_to_nearest_goal = 0  # 距离最近的目标点的距离

    def __init__(self, row, column, parent=None, cost=0, distance_to_nearest_goal=0):
        """
        初始化节点
        :param row: 行
        :param column: 列
        :param parent: 父节点
        :param cost: 距离初始节点的费用
        :param distance_to_nearest_goal: 距离最近的目标点的距离
        """
        self.row = row
        self.column = column
        self.parent = parent
        self.cost_from_initial_node = cost
        self.distance_to_nearest_goal = distance_to_nearest_goal

    def is_same(self, compare):
        """
        判断本节点与另一个节点是否是同一个节点
        :param compare: 用于比较的另一个节点，可以是(row,col)坐标对，也可以是Node实例
        :return: bool, 是否是同一个节点
        """
        if isinstance(compare, Node):
            return compare.row == self.row and compare.column == self.column
        else:
            return compare[0] == self.row and compare[1] == self.column

    def __repr__(self):
        """
        这个函数仅仅是用于显示，将这个节点的信息表示为字符串
        :return:
        """
        return "[" + str(self.row) + "," + str(self.column) + "]"
