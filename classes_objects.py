# class MyClass:

    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

# name = input('Please enter your name: ')
# age = input('Please enter your age: ')
# p1 = MyClass('bk', 23)
# print(p1.name)
# del p1.age
# print(p1.age)
# del p1
# print(p1)


from class2 import Student
class Person(Student):
    pass

p1 = Person()
print(p1.name)
