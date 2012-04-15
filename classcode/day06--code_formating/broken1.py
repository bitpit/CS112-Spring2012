#!/usr/bin/env python

input_list=[]     ##inits list to store all inputs, 
input_number=None #and place to immediately store entry

while input_number != "": #while input isnt not a number
    input_number=raw_input() #get input
    if input_number.isdigit(): #if input is a number
        input_list.append(float(input_number))#append to list

total = 0  #inits place to store sum of all inputs
for num in input_list:
    total+=num     #accumulates sum of all numbers in list
                   #to 'total'

print total/len(input_list) #divides total by length of list
                            #to find average