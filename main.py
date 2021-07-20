# ------------------------------------------------------------------------
# Main maze program
#
# Date:7/20/2021
# Name: Anthony Dawson
# Student ID: 025434121

# ------------------------------------------------------------------------

import convert_maze
import bfs
import dfs
import astar

# ---------CHOOSE WHICH FILE TO TEST------------------
file = "smallMaze.lay"
#file = "mediumMaze.lay"
#file = "bigMaze.lay"

# Call the converter to return a grpah of the maze and the id for the nodes of the start and goal of the maze
graph, start, goal = convert_maze.get_maze(file)

# ----------CHOOSE WHICH ALGORITHM TO RUN--------------
alg = bfs.bfs(graph,start,goal)             # Breadth
#alg = dfs.dfs(graph,start,goal)            # Depth
#alg = astar.astar(graph, start, goal)      # A*

alg.search()

# Getting the solution path and its cost
path = alg.get_path()
cost = len(path)
print("Path Cost:", cost)
print("Path:", path)

# Getting size of maze
maze_file = open(file, "r")
data = maze_file.read()
maze_file.close()

# total length of the file
length = len(data)

# Creating the solved maze---
text = ''

for x in range(length):

    pos = x+1   #The graph index starts at 1

    if pos in path and pos != start:
        text += "."
    elif pos in graph.get_vertices():
        text += graph.get_vertex(pos).get_content()     # will add either ' ' or 'P'
    else:
        text += '%'


print(text)
