from UninformedSearch import UninformedSearch


class DFS(UninformedSearch):

    def add_new_nodes_to_frontier(self, nodes):
        for i in range(0, len(nodes)):  # Add all accessible states to the beginning of the frontier
            self.frontier.insert(i, nodes[i])
