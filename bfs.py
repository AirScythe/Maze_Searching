# ------------------------------------------------------------------------
# Breathe-First Search of maze
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121
# ------------------------------------------------------------------------

import  graph

class bfs(object):

    def __init__(self, maze_graph, start, goal):

        self.maze_graph = maze_graph

        self.start_node = self.maze_graph.get_vertex(start)
        self.goal_node = self.maze_graph.get_vertex(goal)

        self.maze_queue = []
        self.explored = []

        self.expanded_nodes = 0


    def search(self):

        self.maze_queue.append(self.start_node)

        while self.maze_queue != []:

            current_node = self.maze_queue.pop(0)
            self.explored.append(current_node)

            self.expanded_nodes += 1
            print("->", current_node.get_id())

            for c in current_node.get_connections():

                if c not in self.explored:
                    self.maze_queue.append(c)
                    self.explored.append(c)

            if current_node == self.goal_node:
                print("At the end")
                print("Expanded", self.expanded_nodes, "nodes!")


    def get_path(self):
        pass