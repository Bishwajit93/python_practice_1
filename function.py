def greetings_function(name, age):
    print('Welcome', name, 'and your age is', age)

#name = input("Please enter your name: ")
#age = input("Please enter your age: ")
#greetings_function(name , age)
#greetings_function(name = 'Bishwajit Karmaker' , age = 34)

def greetings_with_list(*name):
    print('Welcome', name[1])

#greetings_with_list('a','b','c','d')


def add_numbers(num1, num2):
    return num1 + num2
    # does not excude any command after the return is called

num1 = int(input("Please enter a number: ")) # converting the string type to integer type
num2 = int(input("Please enter another number: "))
print(add_numbers(num1, num2))
