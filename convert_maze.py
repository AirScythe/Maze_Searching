# ------------------------------------------------------------------------
# Covert maze text file to graph structure
#
# Date:7/20/2021
# Name: Anthony Dawson
# ------------------------------------------------------------------------

import graph


def get_maze(file):


    maze_graph = graph.Graph()

    maze_file = open(file, "r")

    # line_offset is the offset to the previous or next line row, the up or down from a vertex
    line_offset = len(maze_file.readline())

    # the position will start at 1
    pos = 1
    row = 1

    # go to start of file
    maze_file.seek(0)

    # track the position id of the start and goal vertex nodes
    start_node = 0
    goal_node = 0

    # Find every blank space ' ', or 'P' and '.' in the file then add a vertex of that position to the graph
    # look by line than look at each character in the line
    for line in maze_file:
        col = 1
        for char in line:

            if char != '%':
                maze_graph.add_vertex(pos, char, row, col)

            if char == 'P':
                start_node = pos

            if char == '.':
                goal_node = pos

            pos += 1
            col += 1

        row += 1

    # Find every connection for each vertex
    maze_spaces = maze_graph.get_vertices()

    # Look for the neighbors of each graph vertex node
    # for the neighbors value add a character for the direction
    for space in maze_spaces:

        if (space + 1) in maze_spaces:
            maze_graph.add_edge(space, space + 1, 'R')

        if (space - 1) in maze_spaces:
            maze_graph.add_edge(space, space - 1, 'L')

        if (space + line_offset) in maze_spaces:
            maze_graph.add_edge(space, space + line_offset, 'D')

        if (space - line_offset) in maze_spaces:
            maze_graph.add_edge(space, space - line_offset, 'U')

    maze_file.close()

    return maze_graph, start_node, goal_node
