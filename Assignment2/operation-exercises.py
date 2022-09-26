#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 00:53:21 2022

@author: dariagogonea
"""
#OPERATION EXERCISES

#1
print(5/2)
print(5.0/2.0)
#Does python output the same values for these?:
    #In this version of python, both operations yielded the same result (2.5).
    #However, in different versions a different value might be given for both 
    #and that is becuase the first operation is an integer division and the 
    #second operation is a float division. This means that the integer division
    #will round to the nearest whole number (ie. 2) and the float division will 
    #result in an answer with a decimal (ie. not an integer; in this case, 2.5)
    
#2
print(2%6)
print(9%4)
print(10%5)
print(5%10)
print(3%3)
#What does the modulo operator (%) do?
    #It codes for the reminder of the integer divisions. For example, 10/5 and 3/3
    #are fully divisible so the answer will be 0 since there are no remainders in 
    #these divisions. Howver, for 2/6 or 9/4, a remainder is given (2 and 1, respectively).
    
#3
print(2**3)
print(5**2)
print(6//3)
print(12//5)
print(12.0//5.0)
#What do these operators do: ** and //?:
    # ** is an exponentual operator. This means that it raises one number to the power of 
    #the other number (ie. 2**3 = 8 and 2x2x2 =8). // is a division operator, it gives the 
    #nearest integer number when two values are being divided (ie. 6//3=2, 12//5 =2).
    
#4
print(3+5+1*4/3)
print(1+2+5*3/9)
#Does python follow order of operations?
    #Yes, python follows order of operations. If it did not follow order of operations, 
    #the answers would be 12 and 3, however, those are not the numbers displayed once the 
    #code is ran.