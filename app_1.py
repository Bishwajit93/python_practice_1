from math import *
import math

#String and print functions

name = 'Bishwajit'
age = 18
print('Hello from Python world.')
print('Welcome',  name.upper())
print('Your age is', age)
print(name.lower(),'How are you? \nHow are you feeling today?')
print(len(name))
print(name.index('j'))
print(name.replace('j', 'g'))


# number and operations
number = 79
print(number)

print(number + 78)
print(number + 78 + 0.945)
result=(number + 78 + 0.945 - 59 * 45 / 9)
print (result)
print(abs(result))
print(max(5,7,3,6,2,1))
print(min(5,7,3,6,2,1))
print(round(3.7))
print(round(3.2))
print(bin(7))

##math import functions
print(sqrt(100))
print(math.pi)


#input fromt the user:
name = input('Input Your Name: ')
age = int(input('your age? '))
print ('Your name is', name ,'and age is', age)


# taking inout and replacing the word as the user wants

sentence = input('Pleas write a sentence: ')
print('Your given sentence is: ' + '"'+sentence+'"')
word1 = input('Please write the word you want to change: ')
word2 = input('Please give the new word: ')
print(sentence.replace(word1, word2))
