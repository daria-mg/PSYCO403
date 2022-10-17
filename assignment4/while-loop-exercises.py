#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:59:19 2022

@author: dariagogonea
"""

# WHILE LOOP EXERCISES

#Q1
iteration = 0
while iteration < 20:
    if iteration < 10:
        print('image1.png')
    elif iteration < 20:
        print('image2.png')
    iteration = iteration + 1

#Q2 
import random 
response = False 

while not response: 
    print("image")
    if random.randint(0,10) == 1:
        response = True 
    elif random.randint(0,10) == 2:
        response = True
#Running it a few of times shows 'image' being printed different times which 
#indicates that the code works as it should work. Once a response of 1 or 2 
#is present, the loop ends. 

#Q3

import random
response  = ''
loop = True
failsafe = -1

while loop:
    failsafe = failsafe + 1
    if failsafe == 5:
        break
    response = random.randint(0,10)
    print(response)
    print('this is an image')
    if response == 1:
        loop = False
    elif response == 2:
        loop = False
    
