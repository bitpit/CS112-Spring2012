#!/usr/bin/env python


#multidimensional arrys mang, w/ a 10x10 griid
grid = []
for i in range(10):   #<--- number of rows
    row = []
    for j in range(10):     #<--- number of columns
        row.append(0)
    grid.append(row)

#grid[2][8] = 99

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        print val,
    print ""

#print grid




#the troube with tron:

#the game loop:
    #setup variables
    #while not done
         #input
         #update
         #draw
         #refresh
