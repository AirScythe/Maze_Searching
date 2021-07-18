# ------------------------------------------------------------------------
# Main maze program
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121
# ------------------------------------------------------------------------

import convert_maze
import bfs


file = "smallMaze.lay"

graph, start, goal = convert_maze.get_maze(file)


b = bfs.bfs(graph,start,goal)
b.search()

#getting size of maze
maze_file = open(file, "r")
data = maze_file.read()
maze_file.close()

length = len(data)

text = ''

for x in range(length):
    if (x+1) in graph.get_vertices():
        text += graph.get_vertex(x + 1).get_content()
    else:
        text += '%'


print(text)
