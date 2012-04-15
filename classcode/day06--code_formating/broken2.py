#!/usr/bin/env python
from random import randint

user_input=int(raw_input())
list=[]        #initiliazing variables

for _ in range(user_input):   #appends input quantity
    list.append(randint(0,20))#of random vars between
                              #1 and 20 to list based on
                              #the number the user entered

print list              #prints list as it is after above

control_var = 1

while control_var:      #while s is not zero
    control_var=0
    for number in range(1,user_input):
        if list[number-1]>list[number]:
            t1=list[number-1]
            t2=list[number]
            list[number-1]=t2
            list[number]=t1
            control_var=1

print list      #prints altered list
