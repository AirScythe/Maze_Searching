# ------------------------------------------------------------------------
# Covert maze text file to graph structure
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121
# ------------------------------------------------------------------------

import graph


def get_maze(file):
    maze_graph = graph.Graph()

    maze_file = open(file, "r")

    # line_offset is the offset to the previous or next line row, up or down for a vertex
    line_offset = len(maze_file.readline())

    pos = 1
    row = 1

    # go to start of file
    maze_file.seek(0)

    # Find every blank space (or P or .) in the file then add to graph
    for line in maze_file:
        col = 1
        for char in line:

            if char != '%':
                maze_graph.add_vertex(pos, char, row, col)

            pos += 1
            col += 1

        row += 1

    # Find every connection for each vertex
    maze_spaces = maze_graph.get_vertices()

    for space in maze_spaces:

        if (space + 1) in maze_spaces:
            maze_graph.add_edge(space, space + 1, 'R')

        if (space - 1) in maze_spaces:
            maze_graph.add_edge(space, space - 1, 'L')

        if (space + line_offset) in maze_spaces:
            maze_graph.add_edge(space, space + line_offset, 'D')

        if (space - line_offset) in maze_spaces:
            maze_graph.add_edge(space, space - line_offset, 'U')

    #maze_graph.graph_summery()

    # print(maze_graph.get_vertex(23).get_dist(maze_graph.get_vertex(72)))

    maze_file.close()

    return maze_graph
