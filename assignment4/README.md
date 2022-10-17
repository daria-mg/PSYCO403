#####CONDITIONAL EXERCISES

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


######LOOP EXERCISES

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
        


###### WHILE LOOP EXERCISES

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
