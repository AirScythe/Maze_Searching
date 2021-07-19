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


file = "smallMaze.lay"
#file = "mediumMaze.lay"
#file = "bigMaze.lay"

graph, start, goal = convert_maze.get_maze(file)


#b = bfs.bfs(graph,start,goal)
b = dfs.dfs(graph,start,goal)

b.search()
p = b.get_path()

cost = len(p)
print("Path Cost:", cost)
print("Path:", p)

#getting size of maze
maze_file = open(file, "r")
data = maze_file.read()
maze_file.close()

length = len(data)

text = ''

for x in range(length):
    pos = x+1
    if pos in p and pos != start:
        text += "."
    elif pos in graph.get_vertices():
        text += graph.get_vertex(pos).get_content()
    else:
        text += '%'


print(text)
