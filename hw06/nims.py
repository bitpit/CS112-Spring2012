#!/usr/bin/env python

"""
nims.py

A simple competitive game where players take stones from stone piles.
by Evan Ricketts, cleaned by Evan Ricketts
"""

pile = int(40)      #defines int pile with 40
print "Number of stones in the pile: ",pile #prints pile
print "Max number of stones per turn: 5"    

turn = int(1)       #control variable used to say who's turn
                    #it currently is, which tells the logic who wins
                    #depending on whos turn it is when the game loop ends

#player 1 turn
while pile > 0:
    pile_str = str(pile)    #type change for printing pile
    one = int(raw_input(pile_str+" stones left. Player 1 [1-5]: ")) #assigns input to int 'one'
    
    turn = 1        #says its player one's turn, so if the loop ends player 2 wins
    
    while one > 5:  #checks to make sure input doesn't exceed max input defined earlier
        print "Invalid number of stones."
        one = int(raw_input(pile_str+" stones left. Player 1 [1-5]: "))
    
    while one > pile: #checks to make sure input doesn't exceed the pile size
        print "Not enough stones"
        one = int(raw_input(pile_str+" stones left. Player 1 [1-5]: "))
    
    pile -= one #assuming earlier checks pass, subtracts int 'one' from the pile
    
    
    #player 2 turn
    if pile > 0:  #assuming the pile isn't empty..
        pile_str=str(pile) #change pile type for printing
        two = int(raw_input(pile_str+" stones left. Player 2 [1-5]: ")) #assign input
                                                                #of user to int 'two'
        turn = 2   #says its player two's turn, so if the loop ends player 1 wins
        
        while two > 5:  #checks to make sure input doesn't exceed max input defined earlier
            print "Invalid number of stones."
            two = int(raw_input(pile_str+" stones left. Player 2 [1-5]: "))
        
        while two > pile:   #checks to make sure input doesn't exceed the pile size
            print "Not enough stones"
            two = int(raw_input(pile_str+" stones left. Player 1 [1-5]: "))
        
        pile-=two   #assuming earlier checks pass, subtracts int 'two' from the pile
    
    else: break   #ends the game loop if the pile is zero when entering player 2's turn
    

if turn == 1:
    print "Player 2 wins!!!"
else: print "Player 1 wins!!!"
