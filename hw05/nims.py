#!/usr/bin/env python
"""
nims.py

A simple competitive game where players take stones from stone piles.
by Evan Ricketts
"""
pile = int(40)
print "Number of stones in the pile: ",pile
print "Max number of stones per turn: 5"
turn = int(1)

while pile > 0:
    pool=str(pile)
    one = raw_input(pool+" stones left. Player 1 [1-5]: ")
    turn = 1
    one = int(one)
    while one > 5:
        print "Invalid number of stones."
        one = raw_input(pool+" stones left. Player 1 [1-5]: ")
        one = int(one)
    while one > pile:
        print "Not enough stones"
        one = raw_input(pool+" stones left. Player 1 [1-5]: ")
        one = int(one)
    pile -= one
    if pile == 0: break
    
    if pile > 0:
        pool=str(pile)
        two = raw_input(pool+" stones left. Player 2 [1-5]: ")
        turn = 2
        two = int(two)
        while two > 5:
            print "Invalid number of stones."
            two = raw_input(pool+" stones left. Player 2 [1-5]: ")
            two = int(two)
        while two > pile:
            print "Not enough stones"
            two = raw_input(pool+" stones left. Player 1 [1-5]: ")
            two = int(two)
        pile-=two
    else: break
    

if turn == 1:
    print "Player 2 wins!!!"
else: print "Player 1 wins!!!"
