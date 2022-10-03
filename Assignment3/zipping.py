#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:45:06 2022

@author: dariagogonea
"""
#ZIPPING EXERCISE

import numpy
import numpy as np

first_item =[]
second_item =[]
imgs_face = ['face1.png']*5 + ['face2.png']*5 +['face3.png']*5 +['face4.png']*5 +['face5.png']*5
imgs_house = ['house1.png']*5 + ['house2.png']*5 + ['house3.png']*5 + ['house4.png']*5 + ['house5.png']*5
imgs_house = ['house1.png' + 'house2.png' + 'house3.png' + 'house4.png' + 'house5.png']
cues = ['cue1']*50 + ['cue2']*50

print(len(imgs_face))
print(len(imgs_house))
print(len(cues))

first_item.extend(imgs_face)
first_item.extend(imgs_house)
first_item.extend(imgs_face)
first_item.extend(imgs_house)
print(first_item)
print(len(first_item))

imgs_faces = ['face1.png', 'face2.png', 'face3.png', 'face4.png', 'face5.png']*5
imgs_houses = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png']*5

second_item.extend(imgs_houses)
second_item.extend(imgs_faces)
second_item.extend(imgs_houses)
second_item.extend(imgs_faces)
print(second_item)
print(len(second_item))

catimgs = list(zip(first_item, second_item, cues))
print (catimgs)
print(len(catimgs))

np.random.shuffle(catimgs)
print(catimgs)