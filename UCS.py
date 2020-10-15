from BFS import BFS


class UCS(BFS):
    def add_new_nodes_to_frontier(self, nodes):
        """
        将节点按费用进行排序
        :param nodes: 节点列表
        :return:
        """
        for i in range(0, len(nodes)):  # 遍历所有新节点
            # Add all accessible states to the beginning of the frontier
            if len(self.frontier) == 0:  # 如果路径中什么也没有，就单纯将这个节点添加进去
                self.frontier.append(nodes[i])
            else:  # 如果路径中已有节点
                for j in range(0, len(self.frontier)):  # 对路径中已有的节点进行遍历
                    # 如果新节点的花费比已有的节点的花费低，则将新节点插入到已有节点的前面。
                    if nodes[i].cost_from_initial_node <= self.frontier[j].cost_from_initial_node:
                        # Sort according to cost
                        self.frontier.insert(j, nodes[i])
                        break
                    # 如果没有一个已有的节点的费用低于新节点，则新节点放在最后一位
                    elif j == len(self.frontier) - 1:
                        self.frontier.append(nodes[i])
