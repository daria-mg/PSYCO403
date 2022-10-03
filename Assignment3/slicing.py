#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:02:20 2022

@author: dariagogonea
"""
# SLICING EXERCISES 

#Q1
list100=list(range(101))
print(list100)

#Q2
print(list100[:10])

#Q3
oddnr=list100[1::2]
print(oddnr[::-1])

#Q4
print(list100[100:96:-1])

#Q5
print(list100[39:44])
print(list100[39:44] == [39, 40, 41, 42, 43])
#The Boolean operation output is True, which indicates 
#that 40th-44th numbers in the list are equal to integers
#39-43. 