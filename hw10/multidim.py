#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""
  
def find_coins(room):
    "returns a list of every coin in the room"
    coins = []
    for x in range(0,len(room)):
        for y in range(0, len(room)):
            if room[x][y] == 1:
                coins.append((y,x))
    return coins



import math
def distance_from_player(player_x, player_y, width, height):
    room = []
    for i in range(0,height):  
        row = []
        for j in range(0,width):
            d1 = math.fabs(player_x-j)
            d2 = math.fabs(player_y-i)
            n = math.sqrt((d1*d1)+(d2*d2))
            row.append(n)
        room.append(row)
    return room
    

    
  
