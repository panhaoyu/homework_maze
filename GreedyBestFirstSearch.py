from InformedSearch import InformedSearch



class GreedyBestFirstSearch(InformedSearch): 
    def add_new_nodes_to_frontier(self, nodes):
       
        for i in range(0, len(nodes)):  # Add all accessible states to the beginning of the frontier
            if len(self.frontier) == 0:
                self.frontier.append(nodes[i])
            else:
                for j in range(0, len(self.frontier)):
                    if nodes[i].distance_to_nearest_goal <= self.frontier[j].distance_to_nearest_goal:  # Sort according to cost
                        self.frontier.insert(j, nodes[i])
                        break
                    elif j == len(self.frontier) - 1:
                        self.frontier.append(nodes[i])

                         
    
   
    
     