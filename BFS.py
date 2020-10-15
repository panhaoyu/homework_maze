from UninformedSearch import UninformedSearch


class BFS(UninformedSearch):

    def add_new_nodes_to_frontier(self, nodes):
        for i in range(0, len(nodes)):  # Add all accessible states to the end of the frontier
            self.frontier.append(nodes[i])
