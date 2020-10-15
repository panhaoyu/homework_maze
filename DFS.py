from UninformedSearch import UninformedSearch


class DFS(UninformedSearch):

    def add_new_nodes_to_frontier(self, nodes):
        """
        添加所有节点
        :param nodes:
        :return:
        """
        for i in range(0, len(nodes)):  # Add all accessible states to the beginning of the frontier
            self.frontier.insert(i, nodes[i])  # 这里只是简单的添加了
