#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 20:41:17 2022

@author: dariagogonea
"""
#ARRAY EXERCISES

#1
import numpy
import numpy as np

mixnums = np.array ([1, 2.0, 3, 4.0, 5, 6.0])
print(mixnums)
#What has happened to the array?
    #The output shows all of the six values above printed as the value
    #and they are then followed by a period (ie. 1 is printed as 1., 
    #2.0 is printed as 2., etc). The integers became floats (however, 
    #they lack the 0) and the floats stayed the same, however, they lost
    #the 0 that they had after the period.

#2
mixtypes = np.array ([1, 2, 3.0, 4.0, '5', '6.0'])
print(mixtypes)
#What has happened to the array? 
    #The integers and floats got printed between '', making them strings 
    #in the output. Every value in this array got printed the way it was 
    #inputted (ie. integers stayed integers and floats stayed floats), 
    #however, every value was between '' even if it was not coded that way. 
#What does python do to arrays with mixed types?
    #Python takes the mixed types and makes them the same in the output. 
    #Integers and floats both became numbers that were followed by a period 
    #and once a string was introduced, all the values were printed between ''.
    #This indicates that arrays should contain the same elements and if they 
    #don't then the output will indicate that they are the same element by 
    #combining them.

#3
oddarray = np.arange(1, 100, 2)
print(oddarray)

#4
logarray = np.logspace (1, 5, 16)
print(logarray)
