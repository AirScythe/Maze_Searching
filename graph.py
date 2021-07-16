# ------------------------------------------------------------------------
# Graph Data Structure
#
# Date:7/12/2021
# Name: Anthony Dawson
# Student ID: 025434121
# ------------------------------------------------------------------------

class Graph(object):
    def __init__(self):
        self.vert_dict = {}
        self.num_vert = 0

    # Node is the name of the vertex and the key
    def add_vertex(self, node, content, row, col):
        new_v = Vertex(node, content, row, col)  # initialize new Vertex object
        self.vert_dict[node] = new_v    # Vertex object added to dictionary as value
        self.num_vert = self.num_vert + 1

    def get_vertex(self, node):
        return self.vert_dict[node]     # Return vertex object

    # adding connection between vertices
    def add_edge(self, from_edge, to_edge, direction):
        self.vert_dict[from_edge].add_neighbor(self.vert_dict[to_edge], direction)     # Adding connection

    def get_vertices(self):
        return self.vert_dict.keys()

    # The connections for each vertex in the dictionary is listed
    def graph_summery(self):
        print("\nGraph Summery:")
        for i in self.vert_dict:    # for each vertex in the dictionary
            for j in self.vert_dict[i].get_connections():   # for each connected vertex in a vertex's dictionary
                print(i, " -> ", j.get_id(), " , ", self.vert_dict[i].get_dir(j))


class Vertex:
    def __init__(self, node, content, row, col):
        self.id = node
        self.adjacent = {}
        self.content = content
        self.row = row
        self.col = col

    def add_neighbor(self, neighbor, direction):
        self.adjacent[neighbor] = direction

    def get_connections(self):
        return self.adjacent

    def get_id(self):
        return self.id

    def get_content(self):
        return self.content

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    # checks if the requested neighbor is connected before returning a the weight
    def get_dir(self, neighbor):

        if neighbor in self.adjacent:   # is the neighbor within the adjacent dictionary?
            return self.adjacent[neighbor]
        else:
            return 0    # return 0 if no connection

    # h(n)
    def get_dist(self, node):
        x = abs(self.row - node.get_row())
        y = abs(self.col - node.get_col())
        return x + y

