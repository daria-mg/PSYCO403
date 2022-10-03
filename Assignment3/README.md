
###### Variable Operations Exercises

Question 1:

``
  sub_code = "sub"
  subnr_int = 2
  subnr_str = "2"

  print(sub_code + subnr_str)
  print(sub_code + subnr_int)
``
sub_nr can be added to sub_code to get the ouput sub2. This works because subnr_str is a string, just like sub_code. subnr_int does not work because this variable is assigned to an integer.


Question 2:

  print(sub_code + " " + subnr_str)
  print(sub_code + " " + subnr_str * 3)
  print((sub_code + subnr_str) * 3)
  print(sub_code * 3 + subnr_str * 3)
  
  
  
###### List Operations Exercises

Question 1:

  numlist = [1,2,3]
  print(numlist)
  print(numlist*2)

Question 2:

  import numpy
  import numpy as np

  numarr = np.array([1,2,3])
  print(numarr)
  print(numarr * 2)
  
Multiply lists results in the items in the list being repeated by the number the list is multiplied by. For example, in this example, the list was multiplied by 2 so [1,2,3] became [1,2,3,1,2,3], each item duplicating. When multiplying arrays, the items in the array undergo the operation. For example, in this question, when multiplying by two, each number in the array doubled. [1,2,3] became [2,4,6]. The number of items in the array stayed the same, only the value of each item increased.

Question 3:

  strlist = ['do','re','mi','fa']
  print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])
  
  print(strlist+strlist)
  
  print([strlist[0]]+[strlist[0], 
        strlist[1]]+[strlist[1], 
        strlist[2]]+[strlist[2], 
        strlist[3]]+ [strlist[3]])
        
  print([[strlist[0],strlist[0]],
        [strlist[1],strlist[1]],  
        [strlist[2],strlist[2]], 
        [strlist[3],strlist[3]]])
 
 

###### Zipping Exercise 

  import numpy
  import numpy as np

  first_item =[]
  second_item =[]
  imgs_face = ['face1.png']*5 + ['face2.png']*5 +['face3.png']*5 +['face4.png']*5 + ['face5.png']*5
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
  
  
  
###### Indexing Exercises

Questiomn 1:
  colors = ['red','orange','yellow', 'green','blue','purple']

Question 2:
  print(colors[4])

Question 3:
  print(colors[4][-2])
  print(colors[4][-1])

Question 4:
  colors.remove('purple')
  colors.insert(5, 'indigo')
  colors.insert(6, 'violet')
  print(colors)
  


###### Slicing Exercises

Question 1:
  list100=list(range(101))
  print(list100)

Question 2:
  print(list100[:10])

Question 3:
  oddnr=list100[1::2]
  print(oddnr[::-1])

Question 4:
  print(list100[100:96:-1])

Question 5:
  print(list100[39:44])
  print(list100[39:44] == [39, 40, 41, 42, 43])

The Boolean operation output is True, which indicates that 40th-44th numbers in the list are equal to integers 39-43. 
