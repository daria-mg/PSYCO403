#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:03:25 2022

@author: dariagogonea
"""
#BOOLEAN EXERCISES

#1
print (1 == 1.0)
print ('1' == '1.0')
#Are 1 and 1.0 equivalent?
    #1 and 1.0 are equivalent because when comparing the two values, 
    #the output is 'True".
#Are "1" and "1.0" equivalent?
    #When comparing if "1" and "1.0" are equivalent, the output is
    #False, which indicates that these two values are not equivalent.
#Why do you think this is?
    #I think that they are not equivalent because 1 and 1.0 is the comparison of 
    #two values that are the same, however, when you compare '1' and '1.0' you are
    #comparing strings that are different from each other. Becuase the strings are 
    #not the same, the output will be false.
  
#2
print (5 == (3+2))
#Are 5 and (3+2) equivalent?
    #The output is True, this means that 5 and (3+2) are equivalent.

#3
print ((1 == 1.0) or ("1" == "1.0") and (5 == (3+2)))
print ((1 == 1.0) or ("1" == "1.0") or (5 == (3+2)))
print ((1 == 1.0) or ("1" == "1.0") and not (5 == (3+2)))
print ((1 == 1.0) and not ("1" == "1.0") and (5 == (3+2)))
print ((1 == 1.0) and ("1" == "1.0") or (5 == (3+2)))
#The above show 5 ways to get "true" as an output.