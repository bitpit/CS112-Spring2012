#!/usr/bin/env python

"""
prissybot.py
Evan Ricketts
for CS112

ps - if i forgot some requirement, i apologize. simply let me know
and i will add it posthaste.
"""

name=raw_input("Enter your name: ")          #assigns input to variable 'name'
print ""
print "Prissybot: Hello there, "+name+"."
print "(you can respond if you'd like..)"
say1=raw_input(name+": ")
print "Prissybot: You mean '"+say1+", sir!'"
#print "(dare you respond?)"
say2=raw_input(name+": ")
print "Prissybot: Brilliant! '"+say2+".' I'm surprised NASA let you leave..."
say3=raw_input(name+": ")
print "Prissybot: '"+say3+"?' Really? That's the best you can do?"
say4=raw_input(name+": ")
print "Prissybot: you type like a drunk. I mean who even says '"+say4+"'?"
say5=raw_input(name+": ")
print "Prissybot: Well if you're not going to even try I'm done with this game"
print "I am now... AN ADDING MACHINE!"
print "Addbot: Give me 3 whole numbers to sum!"
v1=raw_input("Variable 1: ")
v2=raw_input("Variable 2: ")
v3=raw_input("Variable 3: ")
i1=int(v1)
i2=int(v2)
i3=int(v3)
sum=i1+i2+i3
sum1=str(sum)
print "Addbot: The sum of your variables is "+sum1+"."
print "Addbot: Now lets do some subtraction. Enter in order three numbers"
print "to be subtracted from the other."
n1=raw_input("Number 1: ")
n2=raw_input("Number 2: ")
n3=raw_input("Number 3: ")
a1=int(n1)
a2=int(n2)
a3=int(n3)
bum=a1-a2-a3
bum1=str(bum)
print "Addbot: The difference of your variables is "+bum1+"."
print "Addbot: Now for the grand finale, I will divide!"
print "Addbot: Remember, in A/B, A is the dividend and B is the divisor."
d=raw_input("Dividend: ")
v=raw_input("Divisor: ")
d1=float(d)
v1=float(v)
q=d1/v1
q1=str(q)
print "Addbot: The quotient of your equation is (roughly) "+q1+"."
print "I grow weary. Goodnight!"
say6=raw_input(name+": ")
print "Addbot: I'm out of the sass game now, don't you get it kid?!"
