#!/usr/bin/env python

#multidimensional lists -> one of our elements has a couple of elements in it

matrix=["hello",2,0,5,[[10,20],[11,32]], [11,12]]

#print matrix[4][1][0]
#print matrix[5][0]


#tuple - like a list, but are immutable -> 
color = (255, 10, 30)

#color has a 4th channel - ALPHA deals with tranparency


#DICTIONARIES --> same thing as hash maps
eng2sp = {}
eng2sp["one"]= "uno"
eng2sp["two"]="dos"
eng2sp["three"]="tres"

#print eng2sp["one"]
#for k,v in eng2sp.items():
 #   print k,v


people = {'jonah':'stupid',
          'alec':'smelly',
          'jack':'cute',
          'paul':'awesome'}

'''name = raw_input("your name: ")

if name in people:
    print name,"is",people[name]
else:
    print "i dont know you,",name'''

print len(people)
print people.keys()
print people.values()

#string manipulation
s = "Rogistaire Bluntsmurf"
#print s[0:10]
#print s[11:]

'''#objects!!!!
grouping like things together -> having an object that performs all on its own
can have instances of objects -> methods for working with objects
start w/ predefined objects -> SURFACE in pygame is a predefined objects
                                         as is RECTANGLE


