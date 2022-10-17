#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:34:12 2022

@author: dariagogonea
"""

#LOOP EXERCISES

#Q1
myname = 'Daria'
for letter in myname:
    print(letter)

#Q2
myname = 'Daria'
counter = -1
for letter in myname:
    counter = counter + 1
    print (letter)
    print(counter)

#Q3
listnames = ['Amy', 'Rory', 'River']
for name in listnames:
    print(name)
    for letter in name:
        print(letter)

#Q4
listnames = ['Amy', 'Rory', 'River']
for name in listnames:
    print(name)
    lettercounter = -1
    for letter in name:
        lettercounter = lettercounter + 1
        print(letter)
        print(lettercounter)
