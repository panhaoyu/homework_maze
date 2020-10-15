from UninformedSearch import UninformedSearch


class DFS(UninformedSearch):

    def add_new_nodes_to_frontier(self, nodes):
        """
        将新的节点直接按顺序添加到最前面
        :param nodes:
        :return:
        """
        for i in range(0, len(nodes)):  # Add all accessible states to the beginning of the frontier
            self.frontier.insert(i, nodes[i])
