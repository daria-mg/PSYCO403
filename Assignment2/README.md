# ASSIGNMENT 2

## PRINT EXERCISES
Q1:
print("D")
print("a")
print("r")
print("i")
print("a")

Q2: 
Do any variables show up in the Variable Editor?
    No because there are no variables created/used in the code above. The 
    print function is just printing the letters, nothing is being assigned.


## OPERATION EXERCISES
Q1:
print(5/2)
print(5.0/2.0)

Does python output the same values for these?:
    In this version of python, both operations yield the same result (2.5).
    However, in different versions a different value might be given for both 
    and that is because the first operation is an integer division and the 
    second operation is a float division. This means that the integer division
    will round to the nearest whole number (ie. 2) and the float division will 
    result in an answer with a decimal (ie. not an integer; in this case, 2.5)
    
Q2:
print(2%6)
print(9%4)
print(10%5)
print(5%10)
print(3%3)

What does the modulo operator (%) do?
    It codes for the reminder of the integer divisions. For example, 10/5 and 3/3
    are fully divisible so the answer will be 0 since there are no remainders in 
    these divisions. Howver, for 2/6 or 9/4, a remainder is given (2 and 1, respectively).
    
Q3:
print(2**3)
print(5**2)
print(6//3)
print(12//5)
print(12.0//5.0)

What do these operators do: ** and //?:
     ** is an exponentual operator. This means that it raises one number to the power of 
    the other number (ie. 2**3 = 8 and 2x2x2 =8). // is a division operator, it gives the 
    nearest integer number when two values are being divided (ie. 6//3=2, 12//5 =2).
    
Q4:
print(3+5+1*4/3)
print(1+2+5*3/9)

Does python follow order of operations?
    Yes, python follows order of operations. If it did not follow order of operations, 
    the answers would be 12 and 3, however, those are not the numbers displayed once the 
    code is ran.
    
    
## VARIABLE EXERCISES
Q1 and Q2:
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letter5 = 'a'
print (letter1, letter2, letter3, letter4, letter5)

Do any variables show up in the Variable Editor? 
    Yes, variables show up because letters have been assigned to a script.
  
Q4:
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = 'a'
print (letter1, letter2, letter3, letter4, letterX)

Does python have a problem with two (or more) different variables having the same value?
    No, python does not have a problem with two variables having the same value.
    After the code was ran, the two variables ('a') were printed and there were 
    no synthax errors. The same values can be assigned to more than one variable.

Q5:    
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = 's'
print(letter1, letter2, letter3, letter4, letterX)

Did changing the value of letterX change the value of the other variable(s)?
    Changing the value of letterX did not change the value of the other variables
    because if one variable is changed, the others are not affected unless you 
    change the other variables as well. Python printed the other variables the 
    same and only changed the output for letterX. (ie. Daria = Daris)

Q6:
letter1 = 'D'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = '1'
print (letterX, letter1)

letter1 = 'z'
letter2 = 'a'
letter3 = 'r'
letter4 = 'i'
letterX = '1'
print (letterX, letter1)

Did changing the value of letter1 change the value of letterX? What does this tell you about 
python variable assignment?
    Changing the value of letter1 did not change the value of letterX. LetterX stayed the same
    since I did not change the value of letterX, just the value of letter1. This tells me that 
    the values assigned to eahc variable are independent from each other. Changing one value 
    will not affect the other values assigned to other variables.
    

## BOOLEAN EXERCISES
Q1:
print (1 == 1.0)
print ('1' == '1.0')

Are 1 and 1.0 equivalent?
    1 and 1.0 are equivalent because when comparing the two values, 
    the output is 'True".
    
Are "1" and "1.0" equivalent?
    When comparing if "1" and "1.0" are equivalent, the output is
    False, which indicates that these two values are not equivalent.
    
Why do you think this is?
    I think that they are not equivalent because 1 and 1.0 is the comparison of 
    two values that are the same, however, when you compare '1' and '1.0' you are
    comparing strings that are different from each other. Becuase the strings are 
    not the same, the output will be false.
  
Q2:
print (5 == (3+2))

Are 5 and (3+2) equivalent?
    The output is True, this means that 5 and (3+2) are equivalent.

Q3:
print ((1 == 1.0) or ("1" == "1.0") and (5 == (3+2)))
print ((1 == 1.0) or ("1" == "1.0") or (5 == (3+2)))
print ((1 == 1.0) or ("1" == "1.0") and not (5 == (3+2)))
print ((1 == 1.0) and not ("1" == "1.0") and (5 == (3+2)))
print ((1 == 1.0) and ("1" == "1.0") or (5 == (3+2)))

The above show 5 ways to get "true" as an output.


## LIST EXERCISES
Q1:
oddlist = [1, 3, 5, 7, 9]

Did oddlist become a variable?
    Yes, oddlist became a variable since the integers were assigned to it. 
    The print function can be used to print oddlist and the output is the 
    integers that were assigned to oddlist initally. Also, in the variable 
    explorer, oddlist appeared as a variable and the type is 'list'.
    
Q2:
print (oddlist)

Q3:
print(len(oddlist))

How long does python say the list is?
    The output of this is 5. This indicates that the list has 5 items in it.
    
Q4:
print(type(oddlist))

What type of variable does python say oddlist is?
    Output shows that this is a list variable.
    
Q5 and Q6:
intlist = list(range(1,100))
print(intlist)

Does it list all integers between 0 and 100?
    This prints out integers 1 to 99, which are all the integers betweeen 0 and 100.
    in other words, yes, it does list all the integers between 0 and 100.


## DICTIONARY EXERCISES
Q1:
about_me = {
   'name' : 'Daria',
   'age' : '22.0',
   'year of study' : '5',
   'favorite foods' : ['sushi', 'ice cream', 'mango', 'blueberries', 'fried chicken']
   }

Q2:
print(about_me)

Q3:
print(len(about_me))

How does python determine the length of a dictionary?
    Python determines the length of a dictionary by counting how many items are in the 
    dictionary. For example, in this dictionary, the len output is 4 (name, age, year 
    of study, favorite foods). The favorite foods item is a list, however, the amount 
    of items in the list is not included in determining the length of the dictionary.


## ARRAY EXERCISES
Q1:
import numpy
import numpy as np

mixnums = np.array ([1, 2.0, 3, 4.0, 5, 6.0])
print(mixnums)

What has happened to the array?
    The output shows all of the six values above printed as the value
    and they are then followed by a period (ie. 1 is printed as 1., 
    2.0 is printed as 2., etc). The integers became floats (however, 
    they lack the 0) and the floats stayed the same, however, they lost
    the 0 that they had after the period.

Q2:
mixtypes = np.array ([1, 2, 3.0, 4.0, '5', '6.0'])
print(mixtypes)

What has happened to the array? 
    The integers and floats got printed between '', making them strings 
    in the output. Every value in this array got printed the way it was 
    inputted (ie. integers stayed integers and floats stayed floats), 
    however, every value was between '' even if it was not coded that way. 
    
What does python do to arrays with mixed types?
    Python takes the mixed types and makes them the same in the output. 
    Integers and floats both became numbers that were followed by a period 
    and once a string was introduced, all the values were printed between ''.
    This indicates that arrays should contain the same elements and if they 
    don't then the output will indicate that they are the same element by 
    combining them.

Q3:
oddarray = np.arange(1, 100, 2)
print(oddarray)

Q4:
logarray = np.logspace (1, 5, 16)
print(logarray)
