numbers = (1,2,9,4,3,8,6,7,5,1) #tuple allows th repetition of values
print(numbers)

# tuples are immutable means values can't be changed
#numbers[1] = 2 [error-'tuple' object does not support item assignment]

print(numbers[1])
print(len(numbers))
print(type(numbers))


strings=('a','b','c')
print(strings)


boolean = (True, False, True)
print(boolean)


mixed_tuples = (1,2,9,4,True, False,'a','b')
print(mixed_tuples)


# tuple constructor

new_tuple= tuple((1,2,9,4,True, False,'a','b'))
print(new_tuple)
