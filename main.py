# ------------------------------------------------------------------------
# Main maze program
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121
# ------------------------------------------------------------------------

import convert_maze

file = "smallMaze.lay"

g = convert_maze.get_maze(file)

maze_file = open(file, "r")
data = maze_file.read()
maze_file.close()

length = len(data)

text = ''

for x in range(length):
    if (x+1) in g.get_vertices():
        text += g.get_vertex(x+1).get_content()
    else:
        text += '%'


print(text)
