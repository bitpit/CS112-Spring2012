#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    pointIn = True
    if pt[0] >= (box[2]+box[0]):
        pointIn = False
    if pt[1] >= (box[3]+box[1]):
        pointIn = False
    if pt[0] < box[0]:
        pointIn = False
    if pt[1] < box[1]:
        pointIn = False
    
    if pointIn == True:
        return True
    else:
        return False


pt=[12,12]
box=[10,10,10,10]

print point_in_box(pt, box)
