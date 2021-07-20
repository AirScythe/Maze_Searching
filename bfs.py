# ------------------------------------------------------------------------
# Breathe-First Search of maze
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121

# As a guide, used pseudocode from
# "Breadth First Search Algorithm | Shortest Path | Graph Theory" by WilliamFiset
# ------------------------------------------------------------------------

import graph

class bfs(object):

    def __init__(self, maze_graph, start, goal):

        self.maze_graph = maze_graph

        self.start_node = self.maze_graph.get_vertex(start)
        self.goal_node = self.maze_graph.get_vertex(goal)

        # list will track which nodes to process and which have been explored
        self.maze_queue = []
        self.explored = []

        self.expanded_nodes = 0

        # keep track of which vertex nodes came right before each other
        self.prev = {}


    def search(self):

        self.maze_queue.append(self.start_node)
        self.explored.append(self.start_node)

        # The loop will keep going until either all the nodes have been process or the goal has been found
        while self.maze_queue != []:

            # processing the earliest node entered into the queue
            current_node = self.maze_queue.pop(0)

            self.expanded_nodes += 1

            #The node has been expaned and now we are adding their neighbors to the queue
            for n in current_node.get_connections():

                # If the neighbor has not been explored,
                # it's added to the queue, marked explored, and it's prev node is tracked
                if n not in self.explored:
                    self.maze_queue.append(n)
                    self.explored.append(n)
                    self.prev[n] = current_node

            # Break the loop once the goal node has been found
            if current_node == self.goal_node:

                print("Expanded", self.expanded_nodes, "nodes!")

                # The max fringes (frontier) are the unexpanded nodes
                print("Frontier:", len(self.maze_queue))

                break

    # Starting from the goal node, look at the previous node for each node connected to the goal
    def get_path(self):

        self.path = []

        # start at the goal node
        n = self.goal_node

        # Each nod in the 'prev' dictionary marks which node came before it,
        # Get the id of the previous node for each node until we reach the starting node
        while n != self.start_node:
            self.path.append(n.get_id())
            n = self.prev[n]

        self.path.append(n.get_id())

        # reorder the path list so that it begins with the starting node and ends with the goal
        self.path.reverse()

        return self.path