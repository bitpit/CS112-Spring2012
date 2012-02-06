#!/usr/bin/env python

'''
Blastoff! by Evan Johann Sebastian Bach Ricketts
'''
def get_number(number, count)

number=raw_input("What number would you like to count down from? ")
count = int(number)

while count <= 0:
    print "Please enter a positive number"
    return
time = 2000000


while count > 0:
    print count
    count -= 1
    while time > 0:
        time -= 1
    time = 2000000
print "Liftoff!"
