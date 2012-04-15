#!/usr/bin/env python

"""
prissybot.py
Evan Ricketts
for CS112

now known as clearnerbot.py,
a happier, healthier, more user friendly
fork of the prissybot.py code.
"""

#############
##PRISSYBOT##
#############

name=raw_input("Enter your name: ")          #assigns input to variable 'name'
print                                        #clear a bit of space in the prompt
print "Prissybot: Hello there, %s." %name  #prints phrase in addition to user 
print "(you can respond if you'd like..)"   #entered name


say = raw_input(name+": ")          #following prints a series of insults in the 
print "Prissybot: You mean '%s, sir!'" %say    #same manner as the print above
say = raw_input(name+": ")
print "Prissybot: Brilliant! '%s.' I'm surprised NASA let you leave..." %say
say = raw_input(name+": ")
print "Prissybot: '%s?' Really? That's the best you can do?" %say
say = raw_input(name+": ")
print "Prissybot: you type like a drunk. I mean who even says '%s'?" %say
say = raw_input(name+": ")

##################
##ADDING MACHINE##
##################

print "Prissybot: Well if you're not going to even try I'm done with this game"
print "I am now... AN ADDING MACHINE!"      #farily simple 3 print statements
print "Addbot: Give me 3 whole numbers to sum!"

var_1 = int(raw_input("Variable 1: "))    #gets 3 input variables from the user
var_2 = int(raw_input("Variable 2: "))    #and adds them together
var_3 = int(raw_input("Variable 3: "))    #(could be done with lists, or without
reply = str(var_1+var_2+var_3)          #such verbosity, but i like how it works)

print "Addbot: The sum of your variables is %s." %reply #prints sum of user entry


print "Addbot: Now lets do some subtraction. Enter in order three numbers"
print "to be subtracted from the other." #does just about the same thing as the
var_1 = int(raw_input("Number 1: "))       #bit of code above but subtracts rather
var_2 = int(raw_input("Number 2: "))       #than adds the user's input
var_3 = int(raw_input("Number 3: "))
reply = str((var_1-var_2)-var_3)

print "Addbot: The difference of your variables is %s." %reply #prints difference

#dividing is much the same as above, except using floats to express
#the possibility of remainders
print "Addbot: Now for the grand finale, I will divide!"
print "Addbot: Remember, in A/B, A is the dividend and B is the divisor."
dividend = float(raw_input("Dividend: "))
divisor = float(raw_input("Divisor: "))
quotient = str(dividend/divisor)
print "Addbot: The quotient of your equation is (roughly) %s." %quotient
print "I grow weary. Goodnight!"
say=raw_input(name+": ")
print "Addbot: I'm out of the sass game now, don't you get it kid?!"
