from UninformedSearch import UninformedSearch


class BFS(UninformedSearch):
    def add_new_nodes_to_frontier(self, nodes):
        """
        将新的节点按顺序添加到最后面
        :param nodes:
        :return:
        """
        for i in range(0, len(nodes)):  # Add all accessible states to the end of the frontier
            self.frontier.append(nodes[i])
