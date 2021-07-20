# ------------------------------------------------------------------------
# A* Search of maze
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121

# ------------------------------------------------------------------------

import graph

class astar(object):

    def __init__(self, maze_graph, start, goal):

        self.maze_graph = maze_graph

        self.start_node = self.maze_graph.get_vertex(start)
        self.goal_node = self.maze_graph.get_vertex(goal)

        # The queue dictionary will track which nodes to process and their estimated total cost, f() value
        # The explored dictionary will track which nodes have been explored and cost from the starting node, g()
        self.maze_queue = {}
        self.explored = {}

        self.expanded_nodes = 0

        # keep track of which vertex nodes came right before each other
        self.prev = {}


    def search(self):

        #Each value in the maze_queue dictionary has the f() value for each node
        self.maze_queue[self.start_node] = 0 + self.start_node.get_dist(self.goal_node)

        # Each value in the explored dictionary has the g() value for each node
        self.explored[self.start_node] = 0


        # The loop will keep going until either all the nodes have been process or the goal has been found
        while self.maze_queue != {}:

            #picks the node with the lowest estimated cost, f() value
            f = min(self.maze_queue, key = self.maze_queue.get)

            # processing the node with the least estimated cost
            current_node = f

            self.expanded_nodes += 1

            #The node has been expanded and now we are adding their neighbors
            for n in current_node.get_connections():

                # every unexplored node
                if n not in self.explored:

                    # gets the estimated heuristic value h() from the node to the end goal
                    h = n.get_dist(self.goal_node)

                    # increment the distance from the start for the nodes child
                    g = self.explored[current_node] + 1
                    self.explored[n] = g

                    # This adds f as the value for each node in the dictionary, where f = g + h
                    self.maze_queue[n] = g + h

                    # track the node that came right before this neighbor node
                    self.prev[n] = current_node

            # Break the loop once the goal node has been found
            if current_node == self.goal_node:
                print("Expanded", self.expanded_nodes, "nodes!")

                #The max fringes (frontier) are the unexpanded nodes
                print("Frontier:", len(self.maze_queue))

                break

            self.maze_queue.pop(f)


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