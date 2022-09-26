#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:25:25 2022

@author: dariagogonea
"""
#DICTIONARY EXERCISES

#1
about_me = {
   'name' : 'Daria',
   'age' : '22.0',
   'year of study' : '5',
   'favorite foods' : ['sushi', 'ice cream', 'mango', 'blueberries', 'fried chicken']
   }

#2
print(about_me)

#3
print(len(about_me))
#How does python determine the length of a dictionary?
    #Python determines the length of a dictionary by counting how many items are in the 
    #dictionary. For example, in this dictionary, the len output is 4 (name, age, year 
    #of study, favorite foods). The favorite foods item is a list, however, the amount 
    #of items in the list is not included in determining the length of the dictionary.
