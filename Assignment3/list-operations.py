#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 02:01:44 2022

@author: dariagogonea
"""

# LIST OPERATION EXERCISES

#Q1

numlist = [1,2,3]
print(numlist)
print(numlist*2)


#Q2

import numpy
import numpy as np

numarr = np.array([1,2,3])
print(numarr)
print(numarr * 2)
#Multiply lists results in the items in the list being repeated
#by the number the list is multiplied by. For example, in this example,
#the list was multiplied by 2 so [1,2,3] became [1,2,3,1,2,3], easch 
#item duplicating. When multiplying arrays, the items in the array
#undergo the operation. For example, in this question, when multiplying
#by two, each number in the array doubled. [1,2,3] became [2,4,6]. The 
#number of items in the array stayed the same, only the value of each item
#increased.


#Q3

strlist = ['do','re','mi','fa']
print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])
print(strlist+strlist)
print([strlist[0]]+[strlist[0], strlist[1]]+[strlist[1], strlist[2]]+[strlist[2], strlist[3]]+[strlist[3]])
print([[strlist[0],strlist[0]],[strlist[1],strlist[1]],[strlist[2],strlist[2]],[strlist[3],strlist[3]]])
       