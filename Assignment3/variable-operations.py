#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 01:51:28 2022

@author: dariagogonea
"""

#VARIABLE OPERATION EXERCISES

#Q1

sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_str)
print(sub_code + subnr_int)

#sub_nr can be added to sub_code to get the ouput sub2.
#This works because subnr_str is a string, just like sub_code.
#subnr_int does not work because this variable is assigned to an 
#integer.


#Q2

print(sub_code + " " + subnr_str)
print(sub_code + " " + subnr_str * 3)
print((sub_code + subnr_str) * 3)
print(sub_code * 3 + subnr_str * 3)
