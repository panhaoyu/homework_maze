from UninformedSearch import UninformedSearch


class BFS(UninformedSearch):
    def add_new_nodes_to_frontier(self, nodes):
        """
        添加所有节点
        :param nodes:
        :return:
        """
        for i in range(0, len(nodes)):  # Add all accessible states to the end of the frontier
            self.frontier.append(nodes[i])
