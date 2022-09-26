#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:35:57 2022

@author: dariagogonea
"""
#VARIABLE EXERCISES

#1/2
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letter5 = 'a'

print (letter1, letter2, letter3, letter4, letter5)
#Do any variables show up in the Variable Editor? 
    #Yes, variables show up because letters have been assigned to a script.
  
#4
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = 'a'

print (letter1, letter2, letter3, letter4, letterX)
#Does python have a problem with two (or more) different variables having the same value?
    #No, python does not have a problem with two variables having the same value.
    #After the code was ran, the two variables ('a') were printed and there were 
    #no synthax errors. The same values can be assigned to more than one variable.

#5    
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = 's'

print(letter1, letter2, letter3, letter4, letterX)
#Did changing the value of letterX change the value of the other variable(s)?
    #Changing the value of letterX did not change the value of the other variables
    #because if one variable is changed, the others are not affected unless you 
    #change the other variables as well. Python printed the other variables the 
    #same and only changed the output for letterX. (ie. Daria = Daris)

#6
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = '1'

print (letterX, letter1)

letter1 = 'z'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = '1'

print (letterX, letter1)
#Did changing the value of letter1 change the value of letterX? What does this tell you about 
#python variable assignment?
    #Changing the value of letter1 did not change the value of letterX. LetterX stayed the same
    #since I did not change the value of letterX, just the value of letter1. This tells me that 
    #the values assigned to eahc variable are independent from each other. Changing one value 
    #will not affect the other values assigned to other variables.
