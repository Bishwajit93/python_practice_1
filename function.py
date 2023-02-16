def greetings_function(name, age):
    print('Welcome', name, 'and your age is', age)

name = input("Please enter your name: ")
age = input("Please enter your age: ")
greetings_function(name , age)
#greetings_function(name = 'Bishwajit Karmaker' , age = 34)

def greetings_with_list(*name):
    print('Welcome', name[1])

greetings_with_list('a','b','c','d')
