#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)
r = int(n%2)
nd = str(n)
if r==0:
    print "1. Your number, %s, is even." %n
else:
    print "1. Your number, %s, is odd." %n


# 2. If n is odd, double it
if r>0:
    n=(n*2)
    newd=str(n)
    print "2. As your number is odd, I doubled it, yielding "+newd
else:
    print "2. Your number is even, thus I have let it remain "+nd
   


# 3. If n is evenly divisible by 3, add four
if (n%3==0):
    n=n+4
    nd=str(n)
    print "3. As its divisible by 3, I added four to it, producing "+nd+"."
else:
    print "3. It's not evenly divisible by 3..."



# 4. What is grade's letter value (eg. 90-100)


print ("Enter a grade [0-100], and I will convert")
grade = raw_input("it to the proper letter grade: ")
grade = int(grade)
if (grade>96):        #a series of ifs checking the letter grade
    print "Congrats on the A+!"
elif (grade>93 and grade<97):
    print "Congrats on the A!."
elif (grade>89 and grade<94):
    print "A-"
elif (grade>86 and grade<90):
    print "B+"
elif (grade>83 and grade<87):
    print "B"
elif (grade>79 and grade<84):
    print "B-"
elif (grade>76 and grade<80):
    print "C+"
elif (grade>73 and grade<77):
    print "C"
elif (grade>69 and grade<74):
    print "C-"
elif (grade>66 and grade<70):
    print "D+"
elif (grade>64 and grade<67):
    print "D"
else:
    print "F"
