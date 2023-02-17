for letter in 'Hello':
    print(letter)


myList = ['ab','cd','ef','gh']
for letter in myList:
    print(letter)
    if letter == 'gh':
        break

myDict = {
    'name': 'Bishwajit Karmaker',
    'age': 30,
    'uni': 'TU Berlin'
}

for keys in myDict:
    print (keys)


for i in range(10):
    print(i)

for i in range(7, 10):
    print(i)
else:
    print('loop is finisehd')
