#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 09:21:17 2022

@author: dariagogonea
"""

#CONDITIONAL EXERCISES

#Q1
response = 1
if response == 1 or response == 2:
    print('OK')
elif response == "NaN":
    print('subject did not respond')
else:
    print('subject pressed the wrong key')

#Q2
response = 1
if response == 1 or response == 2:
    if response == 1:
        print('correct')
    if response == 2:
        print('incorrect') 
elif response == "NaN":
    print('subject did not respond')
else:
    print('subject pressed the wrong key')

#Q3
#The script does what I expected it to do. In question 1, responses of 1 or 2
#prints out "OK" and responses of "NaN" or anythign else prints out different 
#messages. In question 2, responses of either 1 or 2 prints out a different 
#message depending on what is assigned (ie. 1 prints out correct, 2 prints out
#incorrect).