from InformedSearch import InformedSearch


class AStar(InformedSearch):
    def add_new_nodes_to_frontier(self, nodes):
        """
        将节点按某个距离进行排序，即从起点过来的真实距离加上到目标点的直线距离
        :param nodes:
        :return:
        """
        for i in range(0, len(nodes)):  # Add all accessible states to the beginning of the frontier
            if len(self.frontier) == 0:  # 如果为空，则直接添加
                self.frontier.append(nodes[i])  # 如果本来是空的，直接添加
            else:
                for j in range(0, len(self.frontier)):  # 对所有的进行遍历
                    # 计算两个节点的距离，即从起点过来的真实距离加上到目标点的直线距离
                    if nodes[i].distance_to_nearest_goal + nodes[i].cost_from_initial_node <= \
                            self.frontier[j].distance_to_nearest_goal + self.frontier[j].cost_from_initial_node:
                        # Sort according to cost
                        self.frontier.insert(j, nodes[i])
                        break
                    # 最后一个节点直接添加
                    elif j == len(self.frontier) - 1:
                        self.frontier.append(nodes[i])
