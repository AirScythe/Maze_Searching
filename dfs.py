# ------------------------------------------------------------------------
# Depth-First Search of maze
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121

# As a guide, used pseudocode from
# "Breadth First Search Algorithm | Shortest Path | Graph Theory" by WilliamFiset
# ------------------------------------------------------------------------

import  graph

class dfs(object):

    def __init__(self, maze_graph, start, goal):

        self.maze_graph = maze_graph

        self.start_node = self.maze_graph.get_vertex(start)
        self.goal_node = self.maze_graph.get_vertex(goal)

        self.maze_queue = []
        self.explored = []

        self.expanded_nodes = 0

        self.prev = {}



    def search(self):


        self.maze_queue.append(self.start_node)
        self.explored.append(self.start_node)

        while self.maze_queue != []:

            current_node = self.maze_queue.pop()

            self.expanded_nodes += 1

            #
            for c in current_node.get_connections():

                if c not in self.explored:
                    self.maze_queue.append(c)
                    self.explored.append(c)
                    self.prev[c] = current_node

            if current_node == self.goal_node:
                print("Expanded", self.expanded_nodes, "nodes!")

                # The max fringes (frontier) are the unexpanded nodes in the queue
                print("Frontier:", len(self.maze_queue))

                break


    def get_path(self):
        self.path = []

        at = self.goal_node

        while at != self.start_node:
            self.path.append(at.get_id())
            at = self.prev[at]


        self.path.append(at.get_id())

        #for x in self.path:
        #   print(x)
        self.path.reverse()

        return self.path